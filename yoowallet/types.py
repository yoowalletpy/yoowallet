from abc import ABC
from typing import Any, Dict, List, Optional
from yoowallet.exceptions import (
        AccountInfoError, OperationHistoryError, NoSuchAttribute
)

class Entity(ABC):
    """Abstract class, which represents the skelet of API response entities (like account info)
    
    Args:
        ctx (Dict[Any, Any]): Dictionary, got from raw response 
    
    Attributes:
        ctx (Dict[Any, Any]): Dictionary, got from raw response
        required_scope (List[str]): Required permission for dealing with this entity
    """
    def __init__(self, ctx: Dict[Any, Any], required_scope: List[str]) -> None:
        self._ctx = ctx
        self._required_scope = required_scope
    
    @property
    def ctx(self) -> Dict[Any, Any]:
        """Dictionary from raw request"""
        return self._ctx

    @property
    def required_scope(self) -> List[str]:
        """Required permissions for dealing with this entity"""
        return self._required_scope

    @property
    def keys(self) -> List[str]:
        """Available entity fields. Defining in 'parse' method"""
        return self._keys

    def parse(self) -> None:
        """Parsing provided context"""
        # List of available keys
        self._keys = list(self.ctx.keys())
        for attr in self.ctx.keys():
            setattr(self, "_"+attr, self.ctx[attr])

    def debug(self) -> None:
        """Prints debug information"""
        print(f"[?] Debug for {self.__class__.__name__}:")
        for attr in self.keys:
            print(f"- {attr} ({type(getattr(self, attr))}): {getattr(self, attr)}")

class AccountInfo(Entity):
    """Provides interface for account information
    Args:
        ctx (Dict[Any, Any]): Dictionary, got using '/api/account-info' request
    
    Attributes:
        ctx (Dict[Any, Any]): Dictionary, got using '/api/account-info' request 
    """
    def __init__(self, ctx: Dict[Any, Any]) -> None:
        super().__init__(ctx, ["account-info"])
        try:
            self.parse()
        except Exception as e:
            raise AccountInfoError(f"Failed to parse account info: {e}")

    # Defining fields
    @property
    def account(self) -> str:
        """User’s account number"""
        try:
            return self._account # type: ignore
        except Exception:
            raise NoSuchAttribute("account")

    @property
    def balance(self) -> str:
        """User’s account balance"""
        try:
            return self._balance # type: ignore
        except Exception:
            raise NoSuchAttribute("balance")

    @property
    def currency(self) -> str:
        """User’s account currency code (always 643)"""
        try:
            return self._currency # type: ignore
        except Exception:
            raise NoSuchAttribute("currency")

    @property
    def account_status(self) -> str:
        """The user’s status"""
        try:
            return self._account_status # type: ignore
        except Exception:
            raise NoSuchAttribute("account_status")

    @property
    def account_type(self) -> str:
        """User’s account type"""
        try:
            return self._account_type # type: ignore
        except Exception:
            raise NoSuchAttribute("account_type")

    @property
    def identified(self) -> str:
        """User’s account identification"""
        try:
            return self._identified # type: ignore
        except Exception:
            raise NoSuchAttribute("identified")

    @property
    def balance_details(self) -> Optional[Dict[str, Any]]:
        """Detailed information about the balance (by default, this section is omitted)"""
        try:
            return self._balance_details # type: ignore
        except Exception:
            raise NoSuchAttribute("balance_details")

    @property
    def cards_linked(self) -> Optional[List[Dict[str, Any]]]:
        """Information about bank cards linked to the account"""
        try:
            return self._cards_linked # type: ignore
        except Exception:
            raise NoSuchAttribute("cards_linked")

class OperationHistory(Entity):
    """Provides interface for operation history 
    Args:
        ctx (Dict[Any, Any]): Dictionary, got using '/api/operation-history' request
 
    Attributes:
        ctx (Dict[Any, Any]): Dictionary, got using '/api/operation-history' request
    """
    def __init__(self, ctx: Dict[Any, Any]) -> None:
        super().__init__(ctx, ["operation-history", "operation-details"])
        try:
            self.parse()
        except Exception as e:
            raise OperationHistoryError(f"Failed to parse operation history: {e}")

    @property
    def next_record(self) -> str:
        """The number of the first history record on the next page"""
        try:
            return self._next_record # type: ignore
        except Exception:
            raise NoSuchAttribute("next_record")

    @property
    def operations(self) -> Optional[List[Dict[str, Any]]]:
        """List of operations"""
        try:
            return self._operations # type: ignore
        except Exception:
            raise NoSuchAttribute("operations")

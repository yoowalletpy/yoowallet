from yoowallet.exceptions import MissingFeature

try:
    import requests
except ImportError:
    raise MissingFeature("sync")

from typing import List, Dict, Optional, Any
from datetime import datetime

from yoowallet.exceptions import (
    AccountInfoError, InvalidToken, IllegalParamType,
    IllegalParamStartRecord, IllegalParamRecords, IllegalParamLabel,
    IllegalParamFrom, IllegalParamTill, HistoryTechicalError,
    FailedQuickPayGen
)
from yoowallet.types import (
    AccountInfo, OperationHistory
)

class App:
    """Class for interacting with Yoomoney APIs synchronously.

    Args:
        token (str): Yoomoney application token (can get via Authorizer)
   
    Attributes:
        token (str): Yoomoney application token (can get via Authorizer) 
        headers (Dict[str, str]): Default headers for API requests

    Example:
    ```python
    from yoowallet.sync import App
    from yoowallet.types import AccountInfo
    
    app: App = App("TOKEN")
    if not app.connect():
        raise ValueError('Token is invalid!')
    app_info = app.account_info()
    app_info.debug()
    ```
    """
    def __init__(self, token: str) -> None:
        self.token = token
        self._base_url = "https://yoomoney.ru"
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.token}"
        }

    def account_info(self) -> AccountInfo:
        """Getting account information. Needs at least this scope: ["account-info"]
        
        Returns:
            AccountInfo entity
        """
        # Generating URL
        url = f"{self._base_url}/api/account-info"
        response = requests.post(url=url, headers=self.headers)
        if response.status_code == 200:
            response = response.json()
            return AccountInfo(response)
        elif response.status_code == 401:
            raise InvalidToken 
        else:
            raise AccountInfoError(f"Undefined error, answer: {response}")

    def connect(self) -> bool:
        """Verifying App's token via getting account information
        
        Returns:
            True if token is valid, False if invalid
        """
        try:
            self.account_info()
            return True
        except Exception:
            return False

    def operation_history(
            self,
            type: Optional[List[str]] = None,
            label: Optional[str] = None,
            from_time: Optional[datetime] = None,
            till_time: Optional[datetime] = None,
            start_record: Optional[str] = None,
            records: Optional[int] = None,
            details: Optional[bool] = None
            ) -> OperationHistory:
        """Getting operation history. Needs at least this scope: ["operation-history", "operation-details"]
       
        Example:
        ```python
        from yoowallet.sync import App
        from yoowallet.types import OperationHistory
    
        app: App = App("TOKEN")
        if not app.connect():
            raise ValueError('Token is invalid!')
        app_info = app.operation_history()
        app_info.debug()
        ```

        Args:
            type (Optional[List[str]]): Operation types (deposition or payment)
            label (Optional[str]): Filtering value (custom operation id)
            from_time (Optional[datetime]): Operations from this timestamp
            till_time (Optional[datetime]): Operations till this timestamp
            start_record (Optional[str]): Operations from this number
            records (Optional[int]): Number of history records
            details (Optional[bool]): Show operation details (True or False)

        Returns:
            OperationHistory entity
        """
        # Generating request params
        params = {}
        if type is not None:
            params["type"] = type
        if label is not None:
            params["label"] = label
        # Defining default time format
        time_format = "%Y-%m-%dT%H:%M:%S"
        # Parsing datetimes
        if from_time is not None:
            try:
                params["from"] = datetime.strftime(from_time, time_format)
            except Exception:
                raise IllegalParamFrom("Failed to format input")
        if till_time is not None:
            try:
                params["till"] = datetime.strftime(till_time, time_format)
            except Exception:
                raise IllegalParamTill("Failed to format input")
        if start_record is not None:
            params["start_record"] = start_record
        if records is not None:
            params["records"] = str(records)
        if details is not None:
            params["details"] = details
        # Generating URL
        url = f"{self._base_url}/api/operation-history"
        response = requests.post(url=url, headers=self.headers, data=params) 
        # Errors processing
        if response.status_code in [401, 403]:
            raise InvalidToken
        response = response.json()
        if "error" in response:
            if response["error"] == "illegal_param_type":
                raise IllegalParamType("Try to redefine it in another way")
            elif response["error"] == "illegal_param_start_record":
                raise IllegalParamStartRecord("Try to redefine it in another way'")
            elif response["error"] == "illegal_param_records":
                raise IllegalParamRecords("Try to redefine it in another way'")
            elif response["error"] == "illegal_param_label":
                raise IllegalParamLabel("Try to redefine it in another way'")
            elif response["error"] == "illegal_param_from":
                raise IllegalParamFrom("Try to redefine it in another way'")
            elif response["error"] == "illegal_param_till":
                raise IllegalParamTill("Try to redefine it in another way'")
            else:
                raise HistoryTechicalError("Try again later'")
        return OperationHistory(response)

    def quickpay(
            self,
            sum: float,
            payment_type: str = "AC",
            label: Optional[str] = None,
            success_url: Optional[str] = None
            ) -> Dict[str, Any]: # type: ignore
        """Creating fundraising link
        
        Example:
        ```python
        from yoowallet.sync import App

        app: App = App("TOKEN")
        if not app.connect():
            raise ValueError('Token is invalid!')
        # Generating fundraising for 5 RUB
        payment = app.quickpay(5.0)
        print(f"QucikPay URL is {payment['url']}")
        ```

        Args:
            sum (float): Transfer amount (the amount debited from the sender)
            payment_type (str): PC for a payment from a YooMoney wallet, AC for a payment from a bank card
            label (str): The label that a site or app assigns to a certain transfer
            success_url (str): URL where the user is redirected after the transfer

        Returns:
            Python dictionary with fields: url and amount_due (the amount, that will be received)
        """
        # Getting the number of YooMoney wallet
        receiver: str = (self.account_info()).account
        # Computing the amount to be received
        commissions = {"PC": 0.01, "AC": 0.03}
        amount_due: float = sum*(1-commissions[payment_type])
        # Generating params
        params = {}
        params["receiver"] = receiver
        params["sum"] = sum
        params["quickpay-form"] = "button"
        params["paymentType"] = payment_type
        if label:
            params["label"] = label
        if success_url:
            params["successURL"] = success_url
        response = requests.post(url="https://yoomoney.ru/quickpay/confirm", headers=self.headers, data=params)
        if response.status_code == 200:
            return {"url": response.url, "amount_due": amount_due}
        else:
            # There must be an error handler, but YooMoney didn't provide
            # any error list for QuickPay :(
            raise FailedQuickPayGen(response.status_code)

    def get_by_label(self, label: str) -> Optional[Dict[str, Any]]:
        """Checks whether payment with such label exists

        Args:
            label (str): Lable of needed operation

        Returns:
            Operation details 
        """
        operation = self.operation_history(label = label).operations
        if not operation or len(operation) > 1:
            return
        return operation[0]

import hashlib
from typing import Any, Dict, List
from aiohttp.web import Request, Response
from abc import ABC, abstractmethod
from pprint import pprint

from yoowallet.exceptions import (
            NotificationUnreadable, ReachedAccoundLimit, InvalidHash
        )

# TODO! Implement properties
class Notification:
    def __init__(self, request: Request, secret: str) -> None:
        """Represents notification from Yoomoney API

        Args:
            request (aiohttp.web.Request): Raw Yoomoney notification request 
            secret (str): Secret key, used for notifications verification 
        """
        self.request = request
        self.secret = secret
        self._response = None

    @property
    def type(self) -> str:
        """Notifcation type: p2p-incoming for transfers from wallets, card-incoming for transfers from any bank card"""
        return self.ctx["notification_type"]

    @property
    def operation_id(self) -> str:
        """Operation identifier in your wallet history"""
        return self.ctx["operation_id"]

    @property
    def amount(self) -> str:
        """Amount to be debited to your wallet"""
        return self.ctx["amount"]

    @property
    def datetime(self) -> str:
        """Date and time of the transfer"""
        return self.ctx["datetime"]

    @property
    def sender(self) -> str:
        """Sender’s wallet for transfers from wallets (for transfers from any bank card, the parameter contains an empty string)"""
        return self.ctx["sender"]

    @property
    def label(self) -> str:
        """Payment label (if the label is not present, the parameter contains an empty string)"""
        return self.ctx["label"]

    @property
    def hash(self) -> str:
        """SHA1 hash for verification"""
        return self.ctx["sha1_hash"]

    @property
    def response(self) -> Response:
        """Generated http response"""
        return self._response

    async def process(self) -> None:
        """Method-wrapper for performing notification processing"""
        try:
            self.ctx = await self.request.post()
            required_fields = [
                    "notification_type",
                    "operation_id",
                    "amount",
                    "datetime",
                    "sender",
                    "sha1_hash"
            ]
            for el in required_fields:
                if el not in self.ctx.keys():
                    raise Exception(f"field {el} is missing")
        except Exception as e:
            raise NotificationUnreadable(str(e))
        if "unaccepted" in self.ctx.keys():
            raise ReachedAccoundLimit()
        if not self.check_hash():
            raise InvalidHash() 
        self._response = Response()

    def check_hash(self) -> bool:
        """Checks hash to approve or reject notification"""
        payload = f"{self.type}&{self.operation_id}&{self.amount}&643&{self.datetime}&{self.sender}&false&{self.secret}&{self.label}"
        new_hash = hashlib.sha1()
        new_hash.update(bytes(payload, encoding='utf'))
        result = new_hash.hexdigest()
        if result != self.hash:
            return False
        return True

class Filter(ABC):
    """Abstract filter, used to create new one
    
    Args:
        notification (Notification): Notification object
    """
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    @abstractmethod
    def __call__(self) -> bool:
        """Abstract method, used to call filter
        Returns:
            Boolean which signals whether it's conditions are met"""
        pass

class DefaultFilter(Filter):
    """Default filter, always returns True (handles every single notification)"""
    def __call__(self) -> bool:
        return True

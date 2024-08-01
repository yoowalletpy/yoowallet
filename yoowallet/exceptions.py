# Errors connected with project structure
class MissingFeature(Exception):
    """Signals about missing feature (dependency or code block)"""
    def __init__(self, feature_name: str) -> None:
        message = f"Failed to use feature '{feature_name}' - install it!"
        super().__init__(message)

class InvalidToken(Exception):
    """Signals about invalid token permissions (wrong scope)"""
    def __init__(self) -> None:
        message = "It seems, that the token is invalid for this operation!"
        super().__init__(message)

class NoSuchAttribute(Exception):
    """Signals about missing attribute in entity"""
    def __init__(self, attribute: str) -> None:
        message = f"There is no '{attribute}' attribute!"
        super().__init__(message)
        
# Errors while authorization
# Source: https://yoomoney.ru/docs/wallet/using-api/authorization/request-access-token#response 
class CodeGenError(Exception):
    """Handles code getting errors when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not get code for authorization app: {error_message}"
        super().__init__(message)

class InvalidRequest(Exception):
    """Handles 'invalid_request' error when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"No required field in authorization request: {error_message}"
        super().__init__(message)

class InvalidScope(Exception):
    """Handles 'invalid_scope' error when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"Field 'scope' is invalid in authorization request: {error_message}"
        super().__init__(message)

class UnauthorizedClient(Exception):
    """Handles 'unauthorized_client' error when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"Field 'client_id' is invalid or app is restricted in autohorization request: {error_message}"
        super().__init__(message)

class AuthAccessDenied(Exception):
    """Handles 'access_denied' error when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"Authorization is denied: {error_message}"
        super().__init__(message)

class EmptyToken(Exception):
    """Handles empty token when authorizing app"""
    def __init__(self, error_message: str) -> None:
        message = f"Token is empty: {error_message}"
        super().__init__(message)

# Errors while token revoking
# Source: https://yoomoney.ru/docs/wallet/using-api/authorization/revoke-access-token 
class TokenRevokeBadRequest(Exception):
    """Handles bad request when revoking token"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not revoke invalid token: {error_message}"
        super().__init__(message)

class TokenRevokeUnauthorized(Exception):
    """Handles unauthorized when revoking token"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not revoke token that doesn't exist: {error_message}"
        super().__init__(message)

class TokenRevokeUnknown(Exception):
    """Handles undefined error when revoking token"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not revoke token because of unknown error: {error_message}"
        super().__init__(message)

# Error while account info processing
class AccountInfoError(Exception):
    """Handles error when getting account info"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not get account info: {error_message}"
        super().__init__(message)

# Errors while operation history processing
# Source: https://yoomoney.ru/docs/wallet/user-account/operation-history#errors
class OperationHistoryError(Exception):
    """Handles error when getting operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not get operation history: {error_message}"
        super().__init__(message)

class IllegalParamType(Exception):
    """Handles error when dealing with 'type' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'type' in operation history: {error_message}"
        super().__init__(message)

class IllegalParamStartRecord(Exception):
    """Handles error when dealing with 'start_record' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'start_record' in operation history: {error_message}"
        super().__init__(message)

class IllegalParamRecords(Exception):
    """Handles error when dealing with 'records' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'records' in operation history: {error_message}"
        super().__init__(message)

class IllegalParamLabel(Exception):
    """Handles error when dealing with 'label' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'label' in operation history: {error_message}"
        super().__init__(message)

class IllegalParamFrom(Exception):
    """Handles error when dealing with 'from' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'from' in operation history: {error_message}"
        super().__init__(message)

class IllegalParamTill(Exception):
    """Handles error when dealing with 'till' param in operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Error while processing 'till' in operation history: {error_message}"
        super().__init__(message)

class HistoryTechicalError(Exception):
    """Handles any undefined technical errors when getting operation history"""
    def __init__(self, error_message: str) -> None:
        message = f"Caught techical error when getting operation history: {error_message}"
        super().__init__(message)

# Error while working with QuickPay
class FailedQuickPayGen(Exception):
    """Handles error when generating quickpay link"""
    def __init__(self, http_code: int) -> None:
        message = f"Can not create QuickPay link, server responded with code {http_code}"
        super().__init__(message)

# Errors while HTTP notifications receiving
# Source: https://yoomoney.ru/docs/payment-buttons/using-api/notifications
class NotificationUnreadable(Exception):
    """Handles inability to parse raw notification"""
    def __init__(self, error_message: str) -> None:
        message = f"Can not parse raw notification: {error_message}"
        super().__init__(message)

class ReachedAccoundLimit(Exception):
    """Handles exhaustion of Yoomonwy account limit"""
    def __init__(self) -> None:
        message = "Exhaustion of account limits: try to free up some space in the wallet"
        super().__init__(message)

class InvalidHash(Exception):
    """Handles invalid notification hash"""
    def __init__(self) -> None:
        message = "Notification hash is invalid: it is corrupted or you are under attack"
        super().__init__(message)

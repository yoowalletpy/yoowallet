import aiohttp
from yoowallet.exceptions import (
        TokenRevokeBadRequest,
        TokenRevokeUnauthorized,
        TokenRevokeUnknown
)

async def revoke_token(token: str) -> bool:
    """Revoking token
    
    Args:
        token (str): Yoomoney app token
    Returns:
        True if revoked, error if not
    """
    # Defining base URL
    _base_url = "https://yoomoney.ru"
    # Defining headers
    headers = {
            "Authorization": f"Bearer {token}"
    }
    # Generating URL
    url = f"{_base_url}/api/revoke"
    async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers) as response:
                if response.status == 200:
                    return True
                elif response.status == 400:
                    raise TokenRevokeBadRequest(await response.text())
                elif response.status == 401:
                    raise TokenRevokeUnauthorized(await response.text())
                else:
                    raise TokenRevokeUnknown(await response.text())

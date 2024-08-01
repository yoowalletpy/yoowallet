import aiohttp

from yoowallet.exceptions import (
        CodeGenError, InvalidRequest, InvalidScope,
        UnauthorizedClient, AuthAccessDenied, EmptyToken
)

from typing import List

class Authorizer:
    """Class which helps authorizing Yoomoney app.

    Know more about authorization: https://yoomoney.ru/docs/wallet/using-api/authorization/basics

    Args:
        client_id (str): Yoomoney application id
        redirect_uri (str): URI that the OAuth server sends the authorization result to
        scope (List[str]): Permissions for Yoomoney app, default: ['account-info']
    Returns:
        Object for authorizing Yoomoney app (getting token)
    
    Example: 
    ```python
    import asyncio
    from yoowallet.utils import Authorizer

    async def main():
        client_id = input("Enter client_id: ")
        redirect_uri = input("Enter redirect_uri: ")
        # ! Provide scope if you want not just get account information
        auth = Authorizer(client_id, redirect_uri)
        print(await auth.generate_code_url())
        code = input("Enter code: ")
        print("Your token is:")
        await auth.get_token(code)

    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """
    def __init__(self, client_id: str, redirect_uri: str, scope: List[str] = ["account-info"]) -> None:
        self.client_id = client_id
        self.scope = scope
        self.redirect_uri = redirect_uri
        # Yoomoney URL
        self._base_url = "https://yoomoney.ru"

    async def generate_code_url(self) -> str:
        """Getting special url with a code

        Returns:
            URL from which code can be got
        """
        # Defining headers
        headers = {
                "Content-Type": "application/x-www-form-urlencoded"
        }
        # Generating URL
        url = f"{self._base_url}/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope={'%20'.join([scope for scope in self.scope])}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers) as response:
                if response.status == 200:
                    return str(response.url)
                else:
                    raise CodeGenError(await response.text())

    async def get_token(self, code: str) -> str:
        """Getting token

        Args:
            code (str): Code, got from URL, generated by *generate_code_url* method
        Returns:
            Yoomoney app token
        """
        # Defining headers
        headers = {
                "Content-Type": "application/x-www-form-urlencoded"
        }
        # Generating URL
        url = f"{self._base_url}/oauth/token?code={code}&client_id={self.client_id}&grant_type=authorization_code&redirect_uri={self.redirect_uri}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers) as response:
                response = await response.json()
                if "error" in response:
                    # Checking errors
                    if response["error"] == "invalid_request":
                        raise InvalidRequest(response["error_description"])
                    elif response["error"] == "invalid_scope":
                        raise InvalidScope(response["error_description"])
                    elif response["error"] == "unauthorized_client":
                        raise UnauthorizedClient(response["error_description"])
                    elif response["error"] == "access_denied":
                        raise AuthAccessDenied(response["error_description"])
                # Getting token
                if response["access_token"]:
                    # Saving token as property
                    self.token = response["access_token"]
                    return self.token
                raise EmptyToken(await response.text())

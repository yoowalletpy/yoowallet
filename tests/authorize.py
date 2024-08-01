import asyncio
from yoowallet import App
from yoowallet.utils import Authorizer
from yoowallet.types import AccountInfo

async def main():
    client_id = input("Enter client_id: ")
    redirect_uri = input("Enter redirect_uri: ")
    # ! Provide scope if you want not just get account information
    auth = Authorizer(client_id, redirect_uri)
    print(await auth.generate_code_url())
    code = input("Enter code: ")
    print("Your token is:")
    print(await auth.get_token(code))
    # Testing
    app = App(auth.token)
    if not await app.connect():
        raise ValueError("Token is invalid!")
    app_info: AccountInfo = await app.account_info()
    app_info.debug()

if __name__ == "__main__":
    asyncio.run(main())

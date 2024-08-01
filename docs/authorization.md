# Authorization
First of all, you must create Yoomoney application.
To do it - follow the link: <https://yoomoney.ru/myservices/new>.

Fill in fields (^^don't select OAuth2!^^) and push the button.

Now you must remember client_id and redirect_url, gonna be used
in Authorizer.

Before using yoowallet you must generate ==token==.

When getting token - you connect the application to your wallet and provide
certain permissions. These permissions called ==scope==.

## :lock: Scope
Scope must be provided to ==Authorizer== when generating token as a python list.

This table describes all the supported permissions:

!!! info "Source"
	All permissions are got here:
	<https://yoomoney.ru/docs/wallet/using-api/authorization/protocol-rights>

| Permission        | Description                                                 |
|-------------------|-------------------------------------------------------------|
| account-info      | Getting account info                                        |
| operation-history | Getting operation history                                   |
| operation-details | Getting details about operation                             |
| payment           | Ability to pay in shops and transfer money to other wallets |
| payment-shop      | Ability to buy in registered shops                          |
| payment-p2p       | Ability to transfer money to other wallets                  |

!!! warning "Other permissions"
	Permissions, which have not been metioned
	are not supported (they may work, but ^^do not have to^^)

## :key: Token
Now you are ready to generate token.

The following code snippet will help you:
```python
import asyncio
from yoowallet import App
from yoowallet.utils import Authorizer
from yoowallet.types import AccountInfo

CLIENT_ID = "your client_id here"
REDIRECT_URI = "your redirect_uri here"

async def main():
	# Creating token
	# Provide scope, if you need nore abilities,
	# default is ['account-info']
    auth = Authorizer(
    	CLIENT_ID,
    	REDIRECT_URI
    )
    print(await auth.generate_code_url())
    code = input("Enter code: ")
    print("Your token is:")
    print(await auth.get_token(code))
    # Testing
    app: App = App(auth.token)
    if not await app.connect():
        raise ValueError("Token is invalid!")
    print("App is ready!")

if __name__ == "__main__":
    asyncio.run(main())
```

## :fontawesome-solid-ban: Revoking token
If you generated token with wrong scope or it became useless, 
than the best way is to ==revoke== it.

Perform it using this code:
```python
import asyncio
from yoowallet.utils import revoke_token

TOKEN = "your token here"

async def main():
    if await revoke_token(TOKEN):
        print("Token is revoked!")

if __name__ == "__main__":
    asyncio.run(main()
```

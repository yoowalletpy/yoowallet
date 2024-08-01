# YooWallet
**Simple asynchronous/syncronous python SDK for Yoomoney Wallet and Fundraising (deals with Quickpay) APIs**
> This SDK is unofficial!

### !!! IN DEVELOPMENT !!!
> There are a lot of issues, so use at your own risk! 

### Installation
```bash
# The simplest way:
pip install yoowallet
```
Go to [docs](#docs) to get more info

### Usage
Let's get account info:
```python
import asyncio
from yoowallet import App
from yoowallet.types import AccountInfo

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    app_info: AccountInfo = await app.account_info()
    app_info.debug()
    
if __name__ == "__main__":
    asyncio.run(main())
```
There are way more other functions - go to [docs](#docs)

### Docs
You can access YooWallet documentation here: https://yoowalletpy.github.io

### Sources
- Inspired by: https://github.com/AlekseyKorshuk/yoomoney-api
- Yoomoney Wallet API: https://yoomoney.ru/docs/wallet
- Yoomoney Fundrising API: https://yoomoney.ru/docs/payment-buttons

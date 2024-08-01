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

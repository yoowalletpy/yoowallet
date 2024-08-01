import asyncio
from yoowallet import App

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    payment = await app.quickpay(2.0, label = "some_random_unique_id")
    print(f"[*] Payment link: {payment['url']} ({payment['amount_due']} RUB will be received)")
    
if __name__ == "__main__":
    asyncio.run(main())

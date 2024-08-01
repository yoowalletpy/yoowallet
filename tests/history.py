import asyncio
from yoowallet import App
from yoowallet.types import OperationHistory

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    history: OperationHistory = await app.operation_history()
    history.debug()
    
if __name__ == "__main__":
    asyncio.run(main())

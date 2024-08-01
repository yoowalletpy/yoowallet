import asyncio
from yoowallet.utils import revoke_token

async def main():
    if await revoke_token("TOKEN"):
        print("Token is revoked!")

if __name__ == "__main__":
    asyncio.run(main())

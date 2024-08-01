import asyncio
from yoowallet.notifications import HTTPNotifications, Notification, Filter

# Defining custom filter
class LessThan400(Filter):
    def __call__(self) -> bool:
        return float(self.notification.amount) < 400

async def main():
    server = HTTPNotifications()

    # Handles all notifications
    @server.handle()
    async def general(notif: Notification) -> None:
        print(f"[ {notif.datetime} ] Income {notif.amount} RUB")

    # Handles when amount more than 200
    @server.handle(LessThan400)
    async def less_than_400(notif: Notification) -> None:
        print(f"[*] Got less than 400 RUB: {notif.amount} RUB")

    # Start server on 0.0.0.0:3000
    await server.run("your secret here")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)

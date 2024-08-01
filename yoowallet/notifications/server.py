import asyncio
from aiohttp import web
from aiohttp.web import Request, Response
from typing import Callable, List, Type

from yoowallet.notifications.types import Notification, DefaultFilter, Filter

class HTTPNotifications:
    """Simple HTTP notification server for Yoomoney API.
    More about HTTP notifications: https://yoomoney.ru/docs/payment-buttons/using-api/notifications.
    Firstly, you must setup your notifications here: https://yoomoney.ru/transfer/myservices/http-notification.
    
    Example:
    ```python
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
    ```

    TODO: 
        * Realize multiple filters
    """
    # Will look like: [[filter1, worker1], [filter2, worker2]]
    filters: List[List[Callable]] = []

    def handle(self, filter: Type[Filter] = DefaultFilter) -> Callable:
        """Handling notification events
        
        Args:
            filter (Callable): Filter (always gets Notification as parameter) must return boolean. If not defined - handles every single notification event.
        
        Returns:
            Callable
        """
        def wrapper(worker) -> None:
            self.filters.append([filter, worker])
        return wrapper

    async def check(self, notification: Notification) -> Response:
        """Checking filters when new notification event occured
        
        Args:
            notification (Notification): Received notification

        Returns:
            HTTP response
        """
        for pair in self.filters:
            if pair[0](notification).__call__():
                await pair[1](notification)
        # If no suitable filters sends internal error
        try:
            return notification.response
        except Exception:
            return Response(status=500)

    async def run(self, secret: str, host: str = "0.0.0.0", port: int = 3000, url_pattern: str = "/") -> None:
        """Starting http notification server

        TODO:
            * Realize SSL support
        
        Args:
            secret (str): Secret key, used for notifications verification 
            host (str): Notification server HOST name, default: '0.0.0.0'
            port (int): Notification server port, default: 3000
            url_pattern (str): Url path for sending notifications to, like 0.0.0.0:3000/notifications, default '/'
        """
        self.secret = secret
        routes = web.RouteTableDef()
        app = web.Application()

        # TODO! Implement responsing
        @routes.post(url_pattern)
        async def index(request):
            notification: Notification = Notification(request, self.secret)
            await notification.process()
            return await self.check(notification)

        app.add_routes(routes)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=host, port=port)
        await site.start()
        print(f"[*] HTTPNotification server listening on {host}:{port}{url_pattern} ...")
        await asyncio.Event().wait()

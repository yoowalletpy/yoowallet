# Quick Start

Here will be provided several examples on YooWallet usage.

!!! info "Examples"
    
    All usage examples are available in ==tests/== dir
    in the root of the project

- [Getting account info](#getting-account-info)
- [Getting operation history](#getting-operation-history)
- [QuickPay](#quickpay)
- [Sync API](#sync-api)
- [HTTP notifications](#http-notification-server)

### Getting account info
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

### Getting operation history

!!! tip inline end "More info"
    Go to API Reference to get the complete
    information about parameters

```python
import asyncio
from yoowallet import App
from yoowallet.types import OperationHistory

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    # Operation history without filters
    history: OperationHistory = await app.operation_history()
    print("[*] The entire operation history:")
    history.debug()

    # Operation history for the last hour
    from datetime import datetime
    date = datetime.now()
    date = date.replace(hour = date.hour - 1)
    history: OperationHistory = await app.operation_history(from_time = date)
    print("[*] Operation history for he last hour:")
    history.debug()
    
if __name__ == "__main__":
    asyncio.run(main())
```

### QuickPay

!!! tip "About QuickPay"
    QuickPay is used to receive donates
    via link. You can set ==label== for such link
    and verify it's status in operation history

You can generate link for fundraising:
```python
import asyncio
from yoowallet import App

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    # Set label to get it in operation history
    payment = await app.quickpay(2.0, label = "some_random_unique_id")
    print(f"[*] Payment link: {payment['url']} ({payment['amount_due']} RUB will be received)")
    
if __name__ == "__main__":
    asyncio.run(main())
```

By the way, there is an App method for easily
receiving QuickPay status from operation history:
```python
import asyncio
from yoowallet import App

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Token is invalid!")
    if await app.get_by_label("your label"):
        print("[*] Payment was successfully received")
    
if __name__ == "__main__":
    asyncio.run(main())
```

### Sync API
For some reason you may need for
synchronously using Yoowallet, so there is
support for Sync API. App from Sync API has the
same methods as the async one:

!!! tip inline start "Sync API"
    To use sync API - you must install
    yoowallet in special edition.
    Go to [installation](installation.md) for more info.

```python
from yoowallet.sync import App
from yoowallet.types import AccountInfo

app: App = App("TOKEN")
if not app.connect():
    raise ValueError("Token is invalid!")
app.account_info().debug()
```

### HTTP notification server
!!! danger "WARNING"
    Notification server has not been
    finished yet. Due to a lack of testing
    it may be VERY unstable. So, when server
    is finally written - you will see usage
    info here
But you can still try it via example in ==tests/== dir
**at your own risk**.

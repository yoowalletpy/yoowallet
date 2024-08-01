# Быстрый старт 

Здесь будут приведены некоторые примеры использования YooWallet

!!! info "Примеры"
    
    Все примеры использования доступны в папке ==tests/==
    в корне проекта

- [Получение информации об аккаунте](#_2)
- [Получение истории операций](#_3)
- [QuickPay](#quickpay)
- [Sync API](#sync-api)
- [HTTP уведомления](#http)

### Информация об аккаунте
```python
import asyncio
from yoowallet import App
from yoowallet.types import AccountInfo

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Токен некорректен!")
    app_info: AccountInfo = await app.account_info()
    app_info.debug()
    
if __name__ == "__main__":
    asyncio.run(main())
```

### История операций

!!! tip inline end "Больше информации"
    Обратитесь к API Reference чтобы получить
    всю информацию о параметрах

```python
import asyncio
from yoowallet import App
from yoowallet.types import OperationHistory

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Токен некорректен!")
    # История операций без фильтров
    history: OperationHistory = await app.operation_history()
    print("[*] Полная история операций:")
    history.debug()

    # История операций за последний час
    from datetime import datetime
    date = datetime.now()
    date = date.replace(hour = date.hour - 1)
    history: OperationHistory = await app.operation_history(from_time = date)
    print("[*] История операций за последний час:")
    history.debug()
    
if __name__ == "__main__":
    asyncio.run(main())
```

### QuickPay

!!! tip "QuickPay"
    QuickPay используется для получения донатов
    по ссылке. Вы можете задать ==label== для таких ссылок
    и проверить их статус в истории операций

Вы можете сгенерировать ссылку для сбора денег::
```python
import asyncio
from yoowallet import App

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Токен некорректен!")
    # Устанавливаем label для нахождения в истории операций
    payment = await app.quickpay(2.0, label = "какой_нибудь_уникальный_id")
    print(f"[*] Ссылка для оплаты: {payment['url']} ({payment['amount_due']} руб. будет получено)")
    
if __name__ == "__main__":
    asyncio.run(main())
```

Кстати, в App существует метод для простого
получения статуса QuickPay из истории операций:
```python
import asyncio
from yoowallet import App

async def main(): 
    app: App = App("TOKEN")
    if not await app.connect():
        raise ValueError("Токен некорректен!")
    if await app.get_by_label("ваш label"):
        print("[*] Оплата успешно прошла!")
    
if __name__ == "__main__":
    asyncio.run(main())
```

### Sync API
По какой-то причине вам может понадобиться использовать
Yoowallet синхронно, поэтому существует поддержка Sync API.
Приложение из синхронного API имеет те же методы, что и асинхронное:

!!! tip inline start "Sync API"
    Чтобы использовать синхронный API - вы должны
    установить специальный выйпуск yoowallet.
    Последуйте [установочному гайду](installation.md) чтобы узнать больше.

```python
from yoowallet.sync import App
from yoowallet.types import AccountInfo

app: App = App("TOKEN")
if not app.connect():
    raise ValueError("Токен некорректен!")
app.account_info().debug()
```

### HTTP сервер уведомлений
!!! danger "ВНИМАНИЕ"
    Сервер уведомлений ещё не закончен.
    Из-за отсутствия тестирования он может
    быть ОЧЕНЬ нестабильным. Так, когда сервер
    будет окончательно дописан - вы увидите информацию
    по использованию
Но вы сейчас можете опробовать его при помощи
примеров в папке ==tests/== **на свой страх и риск**.

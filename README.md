# YooWallet
Это простой SDK для работы с API Юмани кошелька и сбора средств на Python.

## Предупреждение
> Данный SDK не является официальным и находится в разработке, поставляется как есть, используйте на свой страх и риск!

### Установка
```bash
# через PyPI
pip install yoowallet

# из исходного кода
git clone <repo>
cd yoowallet
pip install .
```
Вся информация о получении токена и работе с SDK - в [документациии](https://yoowalletpy.github.io) проекта!

### Использование
Получим информацию об аккаунте:
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
О всех функциях и возможностях написано в [документации](https://yoowalletpy.github.io)

### Документация
Вы можете ознакомиться с доументацией YooWallet по ссылке: https://yoowalletpy.github.io

### Источники
- Вдохновлён проектом: https://github.com/AlekseyKorshuk/yoomoney-api
- API Юмани кошелька: https://yoomoney.ru/docs/wallet
- API Юмани сбора средств: https://yoomoney.ru/docs/payment-buttons

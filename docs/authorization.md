# Авторизация
Прежде всего, вы должны создать приложение в Юмани.
Чтобы сделать это - перейдите по ссылке: <https://yoomoney.ru/myservices/new>.

Заполните поля (^^не выбирайте OAuth2!^^) и нажмите на кнопку.

Теперь вам нужно запомнить client_id и redirect_url, 
которые будут использоваться в Authorizer.

Перед использованием yoowallet вы должны сгенерировать ==токен==.

Получая токен - вы подключаете приложение к своему кошельку и 
предоставляете определённые разрешения. Эти разрешения называются ==scope==.

## :lock: Scope
Scope должен быть передан ==Authorizer== при генерации токена в виде python списка.

Эта таблица описывает все поддерживаемые разрешения:

!!! info "Источник"
	Все разрешения взяты отсюда:
	<https://yoomoney.ru/docs/wallet/using-api/authorization/protocol-rights>

| Разрешение        | Описание                                                            |
|-------------------|---------------------------------------------------------------------|
| account-info      | Получение информации об аккаунте                                    |
| operation-history | Получение истории операций                                          |
| operation-details | Получение подробностей об операциях                                 |
| payment           | Возможность платить в магазинах и переводить деньги на другие счета |
| payment-shop      | Возможность покупать в зарегистрированных магазинах                 |
| payment-p2p       | Возможность переводить деньги на другой кошелёк                     |

!!! warning "Другие разрешения"
	Разрешения, которые не были упомянуты -
	не поддерживаются (они могут работать, но ^^не обязаны^^)

## :key: Токен
Теперь вы готовы к генерации токена.

Следующий отрывок кода вам поможет:
```python
import asyncio
from yoowallet import App
from yoowallet.utils import Authorizer
from yoowallet.types import AccountInfo

CLIENT_ID = "ваш client_id"
REDIRECT_URI = "ваш redirect_uri"

async def main():
	# Создание токена
	# Предоставьте scope, если вам нужно больше возможностей
	# стандартное значение - ['account-info']
    auth = Authorizer(
    	CLIENT_ID,
    	REDIRECT_URI
    )
    print(await auth.generate_code_url())
    code = input("Введите код: ")
    print("Ваш токен:")
    print(await auth.get_token(code))
    # Проверка
    app: App = App(auth.token)
    if not await app.connect():
        raise ValueError("Токен некорректен!")
    print("Приложение готово!")

if __name__ == "__main__":
    asyncio.run(main())
```

## :fontawesome-solid-ban: Отозвание токена
Если вы сгенерировали токен с неправильным scope или он стал бесполезным,
то лучший выход - ==отозвать== его.

Проделать это можно при помощи данного кода:
```python
import asyncio
from yoowallet.utils import revoke_token

TOKEN = "ваш токен"

async def main():
    if await revoke_token(TOKEN):
        print("Токен отозван!")

if __name__ == "__main__":
    asyncio.run(main()
```

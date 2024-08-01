# YooWallet SDK
Это простой SDK для работы с API ЮMoney кошелька и сбора средств.
## :warning: Предупреждение
> Данный SDK не является официальным и находится в разработке, поставляется как есть, используйте на свой страх и риск!
## :fontawesome-solid-list: Особенности
- Поддержка асинхронного/синхронного использования
- Утилиты для авторизации приложения ЮMoney (пока только асинхронные)
- Получение информации об аккаунте, списка операций, их деталей
- Выставление счетов для оплаты (QuickPay)
- Сервер для приёма HTTP уведомлений (сырой и пока без поддержки TLS, СЕЙЧАС НЕ ИСПОЛЬЗУЙТЕ!)

## :fontawesome-regular-rectangle-list: Список реализованного
- [x] Авторизация
- [x] Отозвание токена приложения
- [x] Информация об аккаунте
- [x] История операций
- [x] Детали операций
- [ ] Выполнение платежа
- [ ] Обработка платежа
- [x] QuickPay
- [x] HTTP уведомления
    - [x] Сырая реализация
    - [ ] Поддержка TLS

## :information_source: Источники
- Вдохновлён проектом: <https://github.com/AlekseyKorshuk/yoomoney-api>
- ЮMoney кошелёк API: <https://yoomoney.ru/docs/wallet>
- ЮMoney сбор средств API: <https://yoomoney.ru/docs/payment-buttons>

!!! question "Появились вопросы?"
    Присоединяйтесь к [телеграм каналу](https://t.me/yoowallet_python) с разработчиками :simple-telegram: (здесь вы можете задавать вопросы :question:)

Следуйте [гайду по установке](installation.md), чтобы начать использовать YooWallet.
from yoowallet.sync import App
from yoowallet.types import AccountInfo

app: App = App("TOKEN")
if not app.connect():
    raise ValueError("Token is invalid!")
app_info: AccountInfo = app.account_info()
app_info.debug()

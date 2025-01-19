from schwab import auth
import json
import dotenv
from selenium import webdriver

config = dotenv.dotenv_values(".env")

app_key = config["APP_KEY"]
app_secret = config["APP_SECRET"]
callback_url = "https://127.0.0.1:8182/"
token_path = config["TOKEN_PATH"]

client = auth.easy_client(
    app_key, app_secret, callback_url, token_path, webdriver.Firefox
)

history = client.get_price_history_every_day("AAPL")
history.raise_for_status()
print(json.dumps(history.json(), indent=4))

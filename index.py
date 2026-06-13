import time
import requests
from plyer import notification

def check_crypto():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()
    price = response["price"]
    notification.notify(
        title="BTC Price Alert",
        message=f"Bitcoin is currently at ${price}",
        timeout=5
    )
check_crypto()

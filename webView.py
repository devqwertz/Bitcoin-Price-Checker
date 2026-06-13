import requests
from flask import Flask

app = Flask(__name__)

def check_crypto():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()
    return response["price"]

@app.route("/")
def index():
    price = check_crypto()
    return f"Bitcoin is currently at ${price}"

if __name__ == "__main__":
    app.run()

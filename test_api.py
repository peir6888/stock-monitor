import requests
import os
from dotenv import load_dotenv

# 讀取 `.env` 檔案
load_dotenv()
API_KEY = os.getenv("TWELVEDATA_API_KEY")
BASE_URL = "https://api.twelvedata.com"

def fetch_stock_price(symbol):
    url = f"{BASE_URL}/price?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url, timeout=5)  # 設定 5 秒超時
    return response.json()

# 確保這行存在，否則程式不會輸出任何東西！
print(fetch_stock_price("AAPL"))

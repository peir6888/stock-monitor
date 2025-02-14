import aiohttp
from bs4 import BeautifulSoup
import json
from app.services.redis_cache import redis_client

async def fetch_stock_data():
    cached_data = redis_client.get("stock_data")
    if cached_data:
        return json.loads(cached_data)

    url = "https://example-financial-site.com/hot-stocks"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            stocks = []
            for item in soup.select(".stock-item"):
                symbol = item.select_one(".symbol").text
                sector = item.select_one(".sector").text
                price = float(item.select_one(".price").text.replace("$", ""))
                revenue = float(item.select_one(".revenue").text.replace("M", ""))
                stocks.append({"symbol": symbol, "sector": sector, "price": price, "revenue": revenue})

            redis_client.set("stock_data", json.dumps(stocks), ex=3600)
            return stocks

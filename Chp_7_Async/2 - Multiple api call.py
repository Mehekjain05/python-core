import asyncio
async def get_price(symbol):
    print("Fetching price")
    await asyncio.sleep(2)
    print("Price fetched for ticker : ",symbol)


async def get_company_info(symbol):
    print("Fetching company info")
    await asyncio.sleep(3)
    print("Fetched company info for ticker : ",symbol)


async def get_news(symbol):
    print("Fetching news")
    await asyncio.sleep(4)
    print("Fetched news related to ticker : ",symbol)


async def main():
    await get_price("AAPL")
    await get_company_info("AAPL")
    await get_news("AAPL")


if __name__ == "__main__":
    asyncio.run(main())
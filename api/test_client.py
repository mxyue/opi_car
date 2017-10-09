import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://127.0.0.1:8070')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
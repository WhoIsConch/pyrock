from pyrock.aio import Client
import asyncio

client = Client()

async def get_rock():
    rock = await client.get_random_rock()
    print(rock.name)

print("e")

asyncio.run(get_rock())
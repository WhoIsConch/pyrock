from pyrock.aio import Client
import asyncio

client = Client()

async def get_rock():
    rock = await client.get_rock("bedrock")
    print(rock.name)
    await get_rock2()

async def get_rock2():
    rock = await client.get_random_rock()
    print(rock.name + rock.description)

asyncio.run(get_rock())
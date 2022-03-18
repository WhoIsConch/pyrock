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

print("e")

asyncio.get_event_loop().run_until_complete(get_rock())
from pyrock import Client
from pyrock.aio import Client as Client_aio
import asyncio

client = Client()

rock = client.get_random_rock()

print(rock.name)

newrock = client.get_rock("glow rock")

print(newrock.description)

client_aio = Client_aio()

async def get_rock():
    rock = await client_aio.get_rock("bedrock")
    print(rock.name)

asyncio.run(get_rock())
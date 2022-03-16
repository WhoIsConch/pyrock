import aiohttp
from pyrock.wrapper import Client

class Client(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._session = aiohttp.ClientSession()
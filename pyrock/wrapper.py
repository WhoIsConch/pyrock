import requests
import inspect
from .errors import RequestFailed, APIException
from .objects import Rock
import typing
import aiohttp

class Client:
    def __init__(self):
        self._session = requests.session()
        self.api_url = "https://rockapi.apiworks.tech/rock/"
    
    @property
    def session(self) -> typing.Union[aiohttp.ClientSession, requests.Session]:
        return self._session
    
    def get_rock(self, rock_name: str) -> Rock:
        resp = self.session.get(self.api_url + rock_name)

        if inspect.isawaitable(resp):
            async def ret_coro(resp_):
                resp_ = await resp_
                try:
                    return_json_ = await resp_.json()
                    print(return_json_)
                except:
                    raise RequestFailed(f"Request could not be completed: {await resp_.text()}")
                
                if resp_.status != 200:
                    raise APIException(f"Rock API returned an error with status code {resp_.status}: {return_json_['message']}")
                
                return Rock.from_dict(return_json_)
            return ret_coro(resp)
        else:
            try:
                return_json_ = resp.json()
            except:
                raise RequestFailed(f"Request could not be completed: {resp.text()}")
            
            if resp.status_code != 200:
                raise APIException(f"Rock API returned an error with status code {resp.status_code}: {return_json_['message']}")
            
            return Rock.from_dict(return_json_)
            
    def get_random_rock(self) -> Rock:
        resp = self.session.get(self.api_url + "random")

        if inspect.isawaitable(resp):
            async def ret_coro(resp_):
                resp_ = await resp_
                try:
                    return_json_ = await resp_.json()
                except:
                    raise RequestFailed(f"Request could not be completed: {await resp_.text()}")
                
                if resp_.status != 200:
                    raise APIException(f"Rock API returned an error with status code {resp_.status}: {return_json_['message']}")
                
                return Rock.from_dict(return_json_)
            return ret_coro(resp)
        else:
            try:
                return_json_ = resp.json()
            except:
                raise RequestFailed(f"Request could not be completed: {resp.text}")
            
            if resp.status_code != 200:
                raise APIException(f"Rock API returned an error with status code {resp.status}: {return_json_['message']}")
            
            return Rock.from_dict(return_json_)

    def get_top_rock(self) -> Rock:
        resp = self.session.get(self.api_url + "top")

        if inspect.isawaitable(resp):
            async def ret_coro(resp_):
                resp_ = await resp_
                try:
                    return_json_ = await resp_.json()
                except:
                    raise RequestFailed(f"Request could not be completed: {await resp_.text()}")
                
                if resp_.status != 200:
                    raise APIException(f"Rock API returned an error with status code {resp_.status}: {return_json_['message']}")
                
                return Rock.from_dict(return_json_)
            return ret_coro(resp)
        else:
            try:
                return_json_ = resp.json()
            except:
                raise RequestFailed(f"Request could not be completed: {resp.text()}")
            
            if resp.status_code != 200:
                raise APIException(f"Rock API returned an error with status code {resp.status}: {return_json_['message']}")
            
            return Rock.from_dict(return_json_)

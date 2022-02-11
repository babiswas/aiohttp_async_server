from Config.Config import API_LO,API_CATLOG,OAUTH
import aiohttp


class Headers:
   def __init__(self,token):
       self.Accept="application/vnd.api+json"
       self.Authorization="oauth "+token

   def get_header(self):
       return self.__dict__



async def get_all_lo(token):
    headers=Headers(token)
    async with aiohttp.ClientSession(headers=headers.get_header()) as session:
         response=await session.get(API_LO.LO_ENDPOINT)
         json_data=await response.json()
         return json_data


async def get_all_catalogs(token):
    headers=Headers(token)
    async with aiohttp.ClientSession(headers=headers.get_header()) as session:
         response=await session.get(API_CATLOG.CATLOG_ENDPOINT)
         json_data=await response.json()
         return json_data
   
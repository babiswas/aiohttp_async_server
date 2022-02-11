from Config.Config import API_LO,API_CATLOG,OAUTH
import aiohttp


class Headers:
   def __init__(self,token):
       self.Accept="application/vnd.api+json"
       self.Authorization="oauth "+token

   def get_header(self):
       return self.__dict__



async def get_all_lo(token,courseid):
    headers=Headers(token)
    async with aiohttp.ClientSession(headers=headers.get_header()) as session:
         ENDPOINT=''
         if courseid!=None:
            ENDPOINT=API_LO.LO_ENDPOINT+"/"+courseid
         else:
            ENDPOINT=API_LO.LO_ENDPOINT
         response=await session.get(ENDPOINT)
         json_data=await response.json()
         return json_data


async def get_all_catalogs(token,catalogid):
    headers=Headers(token)
    async with aiohttp.ClientSession(headers=headers.get_header()) as session:
         ENDPOINT=''
         if catalogid!=None:
            ENDPOINT=API_CATLOG.CATLOG_ENDPOINT+"/"+catalogid
         else:
            ENDPOINT=API_CATLOG.CATLOG_ENDPOINT
         response=await session.get(ENDPOINT)
         json_data=await response.json()
         return json_data
   
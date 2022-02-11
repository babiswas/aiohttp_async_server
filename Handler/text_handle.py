from aiohttp import web
from prime.http_task import get_all_lo,get_all_catalogs
from Config.Config import OAUTH


async def get_course(request):
   token=OAUTH.TOKEN
   json_data=await get_all_lo(token)
   return web.json_response(json_data)


async def get_catalog(request):
    token=OAUTH.TOKEN
    json_data=await get_all_catalogs(token)
    return web.json_response(json_data)


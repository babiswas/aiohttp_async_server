from aiohttp import web
from prime.http_task import get_all_lo,get_all_catalogs
from Config.Config import OAUTH



async def get_catalog(request):
    token=OAUTH.TOKEN
    catalogid=request.match_info.get('catalogid',None)
    json_data=await get_all_catalogs(token,catalogid)
    return web.json_response(json_data)
from aiohttp import web
from prime.http_task import get_all_lo,get_all_catalogs
from Config.Config import OAUTH



async def get_course(request):
   token=OAUTH.TOKEN
   courseid=request.match_info.get('courseid',None)
   json_data=await get_all_lo(token,courseid)
   return web.json_response(json_data)





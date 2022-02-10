from aiohttp import web

async def get_text(request):
   return web.Response(text="Hello World")


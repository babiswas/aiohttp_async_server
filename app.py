from Handler import text_handle
from aiohttp import web


if __name__=="__main__":
   app=web.Application()
   app.add_routes([web.get('/',text_handle.get_text)])
   web.run_app(app,port=10000)
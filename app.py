from Handler import text_handle
from aiohttp import web


if __name__=="__main__":
   app=web.Application()
   app.add_routes([web.get('/course',text_handle.get_course)])
   app.add_routes([web.get('/catalogs',text_handle.get_catalog)])
   web.run_app(app,port=10000)
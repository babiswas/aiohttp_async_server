from aiohttp import web
from Handler import course_service,catalog_service


if __name__=="__main__":
   app=web.Application()
   app.add_routes([web.get('/course/{courseid}',course_service.get_course)])
   app.add_routes([web.get('/catalog/{catalogid}',catalog_service.get_catalog)])
   web.run_app(app,port=10000)
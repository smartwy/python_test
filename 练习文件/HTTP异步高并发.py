# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from aiohttp import web
import asyncio

async def index(request):
	await asyncio.sleep(1)
	return web.Response(body='<h1>Index</h1>'.encode('utf-8'), content_type='text/html') # 要指定类型，要不然会直接进行get 下载

async def hello(request):
	await asyncio.sleep(1)
	text = '<h1>hello, %s <h1>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index) # 添加请求路由
	app.router.add_route('GET', '/hello/{name}', hello)
	srv = await loop.create_server(app._make_handler(), '127.0.0.1', 8000) # 创建TCP服务
	print('server started at http://127.0.0.1:8000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



import asyncio
import sys
import json
import aiohttp.web
import aiohttp_cors
import hashlib
import secrets
import os

from datetime import datetime, timedelta
from datetime import date
from pprint import pprint

from aiohttp import  web as webhttp

from datetime import datetime
from dateutil import tz

from config.code import MESSAGER_HENDLER
from config.auth import generation_token, descripiton_token

#Logger
import logging
from rich.logging import RichHandler

import resource

HOST = "0.0.0.0"
PORT = 8080
TOKEN = 'L_asJivWBQ8Jwpw-BDzOAOr6Jl-bSiC1YMakNbWCZ78uic2tFrrBg26l50-12YvLb4Y'

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("rich")

async def authentic():
    pass

async def encryption(password):
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

async def websocket_client(request):
    global TOKEN
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    _Token_acess = None
    log.info(f"IP: {request.remote}")
    CHECK_ATH = False
    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                """menssagem from server"""
                data = json.loads(msg.data) 
                if not CHECK_ATH:
                    try:
                        if data['name'] == 'auth':
                            response = await descripiton_token(data['token'])
                            id_user = response['id'] 
                            
                            if response != False:
                                CHECK_ATH = True
                                _Token_acess =  data['token']
                                await ws.send_json({'message': 'Login sucess', 'ok': 'true'})
                                
                            #create folder in storange
                            if os.path.isdir(f'storange/{id_user}') == False:
                               os.system(f'cd storange && mkdir {id_user}')
                               
                    except:
                      await ws.send_json({'message': 'Invalid Acess', 'ok': 'false'})
                      break
                elif data['name'] == 'upload':
                    pass
                elif data['name'] == 'remove':
                    pass
                elif data['name'] == 'create_folder':
                    pass
                elif data['name'] == 'logout':
                    pass
                
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        log.error(f"ERRO MAIN LINE: {line} ERROR: {e}")
    finally:
        await ws.close()
        log.info(f"Disconnected: IP: {request.remote}")

async def login(request):
    """ args email and password == HASH"""
    global MESSAGER_HENDLER
    try:
        post = await request.post()
        email = post.get('email')
        password =  post.get('password')
        password = await encryption(password=password)
        
        token_generation = await generation_token(email=email,password=password)
        payload = {'message': MESSAGER_HENDLER.LOGIN_SUCESS,
                   "bearer": token_generation,
                   "code":200}

        #payload = {'message': MESSAGER_HENDLER.LOGIN_ERRO,"code":401}
        return webhttp.json_response(payload,
            headers={"X-Custom-Server-Header": "Custom data",})
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        log.error(f"{line} Error Token: {e} {line}")
        
        payload = {
                    "message" : MESSAGER_HENDLER.BODY_ERROR,
                    "code"    : 401
                    }
        return webhttp.json_response(payload,
        headers={ "X-Custom-Server-Header": "Custom data",})
        
async def start(app):
    pass

def main():
    try:
        app = aiohttp.web.Application()
        app.on_startup.append(start)
        app.router.add_route('GET', '/client', websocket_client)
        app.add_routes([webhttp.post('/api/login/', login)])
        #app.add_routes([webhttp.post('/api/login/', login)])
        #app.router.add_route('POST', '/api/create', authentic)
        #app.router.add_route('POST', '/api/auth', authentic)
        #app.router.add_route('POST', '/api/upload', authentic)
        #app.router.add_route('POST', '/api/remove', authentic)
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        })

        for route in list(app.router.routes()):
            cors.add(route)
        log.info(f"Server Started Host:{HOST} Port:{PORT} ")
        aiohttp.web.run_app(app, host=HOST, port=PORT)
        
    except Exception as e:
        trace_back = sys.exc_info()[2]
        line = trace_back.tb_lineno
        log.error("ERRO MAIN |LINE: {}|\n|ERROR: {}|".format(line, e))


if __name__ == '__main__':
    main()

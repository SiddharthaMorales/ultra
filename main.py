from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/')

async def ultra(request : Request, name = None):

    client_host = request.client.host

    headers = {'X-hello-world': 'SMG', 'Content-Language':'en-US'}

    if name:
        content = {'ip': client_host, 'greeting': name}
        return JSONResponse(content = content, headers= headers)
    else:
        content = {'ip': client_host}
        return JSONResponse(content = content, headers= headers)

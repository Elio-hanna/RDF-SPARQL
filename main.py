from typing import Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
import codecs
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
import base64

from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

app = FastAPI()
# templates = Jinja2Templates(directory='./')
g = Graph()
g.parse('leagues.xml', format='xml')

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def index():
    f=codecs.open('index.html', 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get('/sparql/{q}')
async def read_items(q):
    if q:
        q = urllib.parse.unquote(q)
        q = q.strip(u'\u200b')
        row = g.query(q)
        json_compatible_item_data = jsonable_encoder(list(row))
        return JSONResponse(content=json_compatible_item_data)
    else:
        return ''
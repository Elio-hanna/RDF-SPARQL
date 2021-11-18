from typing import Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
import codecs
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.templating import Jinja2Templates

from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

app = FastAPI()
# templates = Jinja2Templates(directory="./")
g = Graph()
g.parse('leagues.xml', format='xml')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def form_post():
    f=codecs.open("index.html", 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/sparql")
async def read_items(q: Optional[str] = Query(None)):
    results = {}
    if q:
        print(q)
        row = g.query(q)
        json_compatible_item_data = jsonable_encoder(list(row))
    return JSONResponse(content=json_compatible_item_data)
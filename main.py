from typing import Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

app = FastAPI()
templates = Jinja2Templates(directory="./")
g = Graph()
g.parse('leagues.xml', format='xml')


@app.get("/")
def form_post():
    return templates.TemplateResponse('index.html')

@app.get("/sparql/")
async def read_items(q: Optional[str] = Query(None)):
    results = {}
    if q:
        row = g.query(q)
        json_compatible_item_data = jsonable_encoder(list(row))
    return JSONResponse(content=json_compatible_item_data)
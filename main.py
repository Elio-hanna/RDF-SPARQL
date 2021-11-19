import codecs
from typing import Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
g = Graph()
g.parse('leagues.xml', format='xml')



app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)


@app.get("/")
def form_post():
    f=codecs.open("index.html", 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/sparql/{q}")
async def read_items(q = Query(None)):
    
    print(q)
    if q:
        row = g.query(q)
        json_compatible_item_data = jsonable_encoder(list(row))
        print(json_compatible_item_data)
    return JSONResponse(content=json_compatible_item_data)
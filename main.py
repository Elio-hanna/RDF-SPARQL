import codecs
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from rdflib import Graph

app = FastAPI()
g = Graph()
g.parse('data/leagues.xml', format='xml')

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def load_page():
    f=codecs.open("index.html", 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post('/sparql/')
async def read_items(req: Request):
    req_json = await req.json()
    row = g.query(req_json.get('query'))
    json_compatible_item_data = jsonable_encoder(list(row))
    return JSONResponse(content=json_compatible_item_data)
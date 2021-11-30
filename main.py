import codecs
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from rdflib import Graph
from scripts.querysplitting import QuerySplitting
from scripts.query import Query

app = FastAPI()
g = Graph()
g.parse('data/car-beuty.xml', format='xml')

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

@app.get("/")
def load_main_page():
    f=codecs.open("index.html", 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/extra-feature")
def load_extra_feature():
    f=codecs.open("extra-feature.html", 'r')
    html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post('/sparql')
async def read_items(req: Request):
    req_json = await req.json()
    row = g.query(req_json.get('query'))
    result_query = QuerySplitting.splitting(req_json.get('query'))
    final_result = list(row)
    final_result.insert(0,list(result_query))
    json_compatible_item_data = jsonable_encoder(final_result)
    return JSONResponse(content=json_compatible_item_data)

@app.get('/subject')
def get_subjects():
    subjects = list(g.subjects())
    result = set()
    for x in subjects:
        result.add(x)
    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data)

@app.get('/predicate')
def get_subjects():
    predicate = list(g.predicates())
    result = set()
    for x in predicate:
        result.add(x)
    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data)

@app.get('/object')
def get_subjects():
    objects = list(g.objects())
    result = set()
    for x in objects:
        result.add(x)
    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data)

@app.post('/query')
async def query(req: Request):
    req_json = await req.json()
    print(req_json)
    if (req_json['subject'] != ''):
        sub = "<"+req_json['subject']+">"
    else:
        sub = None
    if (req_json['predicate'] != ''):
        pred = "<"+req_json['predicate']+">"
    else:
        pred = None
    if (req_json['object'] != ''):
        # obj = "<"+ req_json['object']+">"
        obj = req_json['object']
    else:
        obj = None

    final_result = Query.query(g,sub,pred,obj)
    json_compatible_item_data = jsonable_encoder(final_result)
    return JSONResponse(content=json_compatible_item_data)
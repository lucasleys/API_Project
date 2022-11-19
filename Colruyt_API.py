from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path
from pydantic import BaseModel


class given_product(BaseModel):
    naam: str
    prijs: float
    categorie: str | None = None


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = {1: {'categorie': 'zuivel', 'product': 'kaas', 'prijs': '1.50'},
            2: {'categorie': 'vlees', 'product': 'biefstuk', 'prijs': '2.30'},
            3: {'categorie': 'diepvries', 'product': 'frieten', 'prijs': '1.20'},
            4: {'categorie': 'koeling', 'product': 'ham', 'prijs': '3.40'},
            5: {'categorie': 'zuivel', 'product': 'melk', 'prijs': '1.30'},
            6: {'categorie': 'vlees', 'product': 'kip', 'prijs': '2.50'},
            7: {'categorie': 'diepvries', 'product': 'erwten', 'prijs': '0.70'},
            8: {'categorie': 'koeling', 'product': 'yoghurt', 'prijs': '1.10'}}

locations = {1: {'postcode': '2350', 'locatie': 'vosselaar'},
             2: {'postcode': '2440', 'locatie': 'geel'},
             3: {'postcode': '2600', 'locatie': 'berchem'},
             4: {'postcode': '6280', 'locatie': 'gerpinnes'},
             5: {'postcode': '9900', 'locatie': 'eeklo'},
             6: {'postcode': '8370', 'locatie': 'blankenberge'},
             7: {'postcode': '3500', 'locatie': 'hasselt'},
             8: {'postcode': '5300', 'locatie': 'andenne'}}



@app.get("/{categorie}/{product}/{prijs}")
async def get_product(categorie: str = Query(default=None), product: str = Query(default="n"), prijs : float = Query(default=0)):
    cat_results = {}
    prijs_results = {}
    print("categorie: " + categorie)
    if categorie:
        for i in products:
            if categorie == products[i]['categorie']:
                cat_results[i] = products[i]
        return cat_results
    if product:
        for i in products:
            if product == products[i]['product']:
                return products[i]['product'] + products[i]['prijs']
    if prijs:
        for i in products:
            if prijs == products[i]['prijs']:
                prijs_results[i] = products[i]
        return prijs_results


@app.get("/{location}")
async def get_nearby_location(location):
    if location:
        for i in locations:
            if location == locations[i]['postcode']:
                return locations[i]['postcode'] + " " + locations[i]['locatie']
            return{"error":"no location nearby"}

@app.post("/")
async def create_product(wanted_product: given_product):
    wanted_products = {}
    for i in range(50):
        if wanted_product.dict() not in wanted_products.values():
            wanted_products.setdefault(i, wanted_product)
            return wanted_product
        return {"error":"product already listed"}


from fastapi import FastAPI, HTTPException
from model_egg import ModelEgg
from db import database

app = FastAPI()


@app.get("/eggs")
def fetch_eggs():
    db = database()
    eggs = db.warehouse.find()
    res = []
    for egg in eggs:
        data = {
            "breeding": egg["breeding"],
            "color": egg["color"],
            "immat": egg["immat"],
        }
        res.append(data)
    return res


@app.post("/eggs/")
def create_egg(egg: ModelEgg):
    db = database()
    if db.warehouse.find_one({"immat": egg.immat}) is not None:
        raise HTTPException(
            status_code=409, detail="Registration is already registered"
        )
    db.personnes.insert_one(egg.dict())
    return egg.dict()


@app.get("/eggs/{immat}")
def fetch_personne_by_immat(immat: str):
    db = database()
    egg = db.warehouse.find_one({"immat": immat})
    res = {
        "breeding": egg["breeding"],
        "color": egg["color"],
        "immat": egg["immat"],
    }
    return res


@app.delete("/eggs/{immat}")
def delete_personne_by_immat(immat: str):
    db = database()
    db.warehouse.delete_one({"immat": immat})


@app.put("/eggs/{immat}")
def update_personne_by_immat(immat: str, egg: ModelEgg):
    db = database()
    db.warehouse.update_one({"immat": immat}, {"$set": egg.dict()})
    return egg.dict()

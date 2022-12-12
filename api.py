from fastapi import FastAPI,Path,Query
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:str

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None

inventory={}

@app.get("/get-item/{id}")
def get_item(id:int=Path(None, description="This is an item")):
    return inventory[id]

# Finding a particular query

@app.get("/get-by-name")
def get_item(name:str):
    for id in inventory:
        if inventory[id].name==name:
            return inventory[id]
    return {"Data":"Not found"}

#Post request

@app.post("/create-item/{id}")
def create_item(id:int, item:Item):
    if id in inventory:
        return {"Error":"Item already exists"}
    inventory[id]=item
    return inventory[id]

#PUT request

@app.put("/update-item/{id}")
def update_item(id:int, item:UpdateItem):
    if id not in inventory:
        return {"Error":"Item does not exist"}
    if item.name!=None:
        inventory[id].name=item.name
    if item.price!=None:
        inventory[id].price=item.price
    if item.brand!=None:
        inventory[id].brand=item.brand
    return inventory[id]

#DELETE request

@app.delete("/delete-item")
def delete_item(id:int= Query(..., description="The id of item to delete"),ge=0):
    if id not in inventory:
        return {"Error":"ID doest not exist"}
    del inventory[id]
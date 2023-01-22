from fastapi import FastAPI, Path, Query, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass, field
from enum import Enum

import domains
"""


uvicorn main:app --reload


"""

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello":"GET"}

@app.post("/")
async def post():
    return {"Hello":"POST"}

@app.put("/")
async def put():
    return {"Hello":"PUT"}


@app.get("/items/{item_id}")
async def get_item(item_id: str = Path(None, 
                    description="The id of the item you'd like to view."), 
                    q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/get-by-name")
async def get_item(*,name:Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]

inventory = {}

class FoodsEnum(str, Enum):
    fruit = "fruit" 
    chocolate = "chocolate"
    chicken = "chicken"

@app.get("/food/{food_name}")
async def get_food_name(food_name: FoodsEnum):
    if food_name == FoodsEnum.chicken:
        return {"food_name": food_name, "message": "You love chicken!!!"}
    elif food_name.value == "chocolate":
        return {"food_name": food_name, "message": "You like sweets."}
    else:
        return {"food_name": food_name, "message": f"You are a {food_name} lover."}


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]=None
    
class UpdateItem(Item):
    name: Optional[str]=None
    price: Optional[float]=None
    
    
@app.post("/insert-item/{item_id}")
def insert_item(item_id:int, item:Item):
    if item_id in inventory:
        return {"Error": "item_id already exists."}
    inventory[item_id] = item
    return inventory[item_id]
    
@app.put("/update-item/{item-id}")
def update_item(item_id:int, item:UpdateItem):
    if item_id not in inventory:
        # return {"Error": "item_id does not exist."}
        raise HTTPException(status_code=404, detail="item_id not found.")
    # inventory[item_id] = item
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id:int=Query(..., description="ID of item to be deleted.", gt=0)):
    if item_id not in inventory:
        return {"Error": "item_id does not exist."}
    else:
        del inventory[item_id]


@dataclass
class InventoryItem:
    name: str
    price: float = field(repr=False, compare=False)
    size: str
    




if __name__ == "__main__":
    """
    # Build the image
    docker build -t domaingen .
    
    # Run the image container
    docker run -p 8000:8000 domaingen
    
    # Must specify the port and host address:
    """    
    uvicorn.run(app, port=8000, host="0.0.0.0")

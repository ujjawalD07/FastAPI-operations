from fastapi import FastAPI,Path,Query
from typing import Optional
from pydantic import BaseModel
from geopy.geocoders import Nominatim
import uvicorn

geolocator = Nominatim(user_agent="geoapiExercises")
app=FastAPI()

class Route(BaseModel):
    latitude:str
    longitude:str

def route(lt,ln):
    location = geolocator.geocode(lt+","+ln)
    return location

@app.get("/")
def home():
    return {"message":"Hello"}

@app.get("/find")
def find_route(lt:str, ln:str):
    result = str(route(lt,ln))
    print(type(result))
    return {'result': result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
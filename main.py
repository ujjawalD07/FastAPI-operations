from fastapi import FastAPI,Path,Query,Request,Form
from typing import Optional
from pydantic import BaseModel
from geopy.geocoders import Nominatim
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

geolocator = Nominatim(user_agent="geoapiExercises")
app=FastAPI()

templates= Jinja2Templates(directory="htmldirectory")

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
    # print(type(result))
    return {'result': result}

@app.get("/submit",response_class=HTMLResponse)
async def get_submit(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/submit",response_class=HTMLResponse)
async def post_submit(request:Request, latitude: str=Form(...), longitude: str=Form(...)):
    print(f'latitude:{latitude}')
    print(f'longitude:{longitude}')
    result = str(route(str(latitude),str(longitude)))
    # print(type(result))
    return templates.TemplateResponse("index.html",{"request":request,"result":result})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
from fastapi import FastAPI
from routers import users, products, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

#uvicorn main:app --reload

#se integran los otros dos apis 

app = FastAPI()

#Routers 
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#forma para exponer recursos estaticos 
#http://127.0.0.1:8000/static/images/vainilla.JPEG

app.mount("/static", StaticFiles(directory="static"), name="static") 




@app.get("/")
async def read_root():         #asincronia, trabaja en segundo plano 
    return {"Hello": "World"}  #devolvio un JSON

"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

"""

"""
#actualiza con crt + s no con play 

@app.get("/url")
async def url():                    #asincronia, trabaja en segundo plano 
    return {"url":"https://mouredev.com/python"}

http://127.0.0.1:8000
http://127.0.0.1:8000/docs  es como el thunder client
http://127.0.0.1:8000/redoc

"""

#source venv/bin/activate activar el entorno virtual
#abrir las carpetas hasta llegar donde esta main.py 
#cd venv/Backend/FastAPI 

# activar el server desde FastAPI
#uvicorn main:app --reload

#autenticar es identificar
#autorizar es permisos 

#mongodb://localhost:27017

#iniciar y cerrar el mongodb en localhost
#docker start mongodb 
#docker stop mongodb


#usuario en mongodb data
#test
#alejandrojfs26_db_user


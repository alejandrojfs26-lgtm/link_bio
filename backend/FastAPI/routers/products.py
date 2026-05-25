from http.client import responses
from urllib import response
from sys import prefix
from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"],  
                   responses={404: {"message": "No encontrado"}})

#tags para separar por partes 


products_list = ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5",]

@router.get("/")
async def products():
    return products_list

#uvicorn products:app --reload
#con el router integramos dos servicios 

@router.get("/{id}")
async def products(id:int):
    return products_list[id]


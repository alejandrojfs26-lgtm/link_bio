from logging import error
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# inicia el server : uvicorn users:app --reload

# entidad user 

class User(BaseModel): 
    id: int
    name: str
    surname: str
    url: str
    age: int 

users_list = [User(id=1, name="Viggo", surname="fuentes", url="https://moure.dev", age=34),
            User(id=2, name="Alejandro", surname="fuentes", url="https://moure.dev", age=32),
            User(id=3, name="Alejandro", surname="fuentes", url="https://moure.dev", age=33)]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Alejandro", "surname": "fuentes", "url":"https://moure.dev","age":34},
           {"name": "Alejandro", "surname": "fuentes", "url":"https://moure.dev","age":34},
            {"name": "Alejandro", "surname": "fuentes", "url":"https://moure.dev","age":34}]

@router.get("/users")
async def users():
    return users_list

#path
#buscar una sola obligatoria / /// /

#http://127.0.0.1:8000/user/1

@router.get("/user/{id}")
async def user(id:int):
    return search_user(id)
    
#query
#para buscar un rango de paginacion que no es obligatorio 
# comienza (?) esto para concatenar (&) 
    
#http://127.0.0.1:8000/userquery/?id=1

@router.get("/userquery/")
async def user(id:int):
    return search_user(id)


#search para buscar 

def search_user(id: int): 
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except: 
        return {"error":  "no hay usuario"}

#se crea la misma operacion dos veces mediante la path y la query 

#http://127.0.0.1:8000/users/?id=1&name=alejandro otra forma de la llamada 

#post para agregar usuario 

@router.post("/user/", status_code=201) #agregar errores al path
async def user(user: User):
    existing_user = search_user(user.id)
    if not isinstance(existing_user, dict): # Si no es un diccionario de error, es un User
        raise HTTPException(status_code=409, detail="El usuario ya existe")
    
    users_list.append(user)
    return user

#put actualizar usuario 

@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id: 
            users_list[index] = user
            found = True
    
    if not found: 
        raise HTTPException(status_code=404, detail="No se ha actualizado el usuario")
    
    return user

#delete borrar usuario


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id: 
            del users_list[index] 
            found = True
            break
        
    if not found: 
        raise HTTPException(status_code=404, detail="No se ha eliminado el usuario")
    
    return {"message": "Usuario eliminado"}









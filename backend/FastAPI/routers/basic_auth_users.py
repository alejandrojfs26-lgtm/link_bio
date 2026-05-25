from gc import disable
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basicauth", 
                   tags=["basicauth"],  
                   responses={404: {"message": "No encontrado"}})


router = APIRouter()

#estandar de autenticacion 

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel): 
    username: str
    full_name: str
    email: str
    disable: bool 

#base de datos de usuario 

class UserDB(User): 
    password : str


users_db = {
    "mouredev": { 
        "username": "mouredev", 
        "full_name": "Brais Moure",
        "email": "braismoure@gmail.com",
        "disable": False, 
        "password": "123456"    
        
    },
    "mouredev2": { 
        "username": "mouredev2", 
        "full_name": "Brais Moure 2",
        "email": "braismoure2@gmail.com",
        "disable": True, 
        "password": "654321"    
        
    }

}

#buscar el username con post en el liteclient 
#depends dependencia 

def search_user_db(username: str):
    if username in users_db: 
        return UserDB(**users_db[username]) 


def search_user(username: str):
    if username in users_db: 
        return User(**users_db[username]) 


async def current_user(token: str = Depends(oauth2)): 
    user = search_user(token)
    if not user:    
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="La credencial es invalida",
        headers={"WwW-Authenticate": "Bearer"})
    return user 

    if user.disable: 
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="usuario inactivo")


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:     
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto"
        )

    user = search_user_db(form.username)
    if not user or not form.password == user.password: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="La contraseña no es correcta"
        )

    return {"access_token": user.username, "token_type": "bearer"}
     
@router.get("/users/me")
async def me(user: User = Depends(current_user)): 
    return user

"""
revisar los datos que se añadieron em el liteclient 
Key: Autorization 
Value: Bearer mouredev """ 
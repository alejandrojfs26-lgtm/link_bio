from jose import JWTError
from gc import disable
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 
SECRET = "8c554c347db2f5a38ec4da28c0b28e67d88f46c332458a7732dff6f590f6130d"

router = APIRouter(prefix="/jwtauth", 
                   tags=["jwtauth"],  
                   responses={404: {"message": "No encontrado"}})

#openssl rand -hex 32
#genera un numero en el terminal 

router = APIRouter()

#encriptacion de autenticacion 
#uvicorn main:app --reload abrir el server general 

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$uDvhFogKdr67HtHzKU3Xr.G2YMFxuCRVEWpYUpGrtJ6KUsCwUIAqm"    
        
    },
    "mouredev2": { 
        "username": "mouredev2", 
        "full_name": "Brais Moure 2",
        "email": "braismoure2@gmail.com",
        "disable": True, 
        "password": "$2a$12$5Zc2jclfPi089hlLRQTlMedJprzuTwbWVHOBs7/72AxvWnV.7nVeS"    
        
    }

}


def search_user_db(username: str):
    if username in users_db: 
        return UserDB(**users_db[username]) 

def search_user(username: str):
    if username in users_db: 
        return User(**users_db[username]) 



async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La credencial es invalida",
            headers={"WwW-Authenticate": "Bearer"})


    try: 
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None: 
            raise exception

        

    except JWTError: 
        raise exception


    return search_user(username)


async def current_user(user: User = Depends(auth_user)): 
   
    if user.disable: 
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="usuario inactivo")
    
    return user 


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:     
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto"
        )

    user = search_user_db(form.username)

  
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="La contraseña no es correcta")

    "access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)"

    "expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)"
    
    access_token = {"sub": user.username, 
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

# Se añade jwt.encode() para codificar el diccionario en un token real de texto
# uvicorn jwt_auth_users:app --reload
    



@router.get("/users/me")
async def me(user: User = Depends(current_user)): 
    return user


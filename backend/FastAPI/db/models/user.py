from pydantic import BaseModel
from typing import Optional

class User(BaseModel): 
    #id: str | None = None   #puede ser opcional asi 
    id: Optional[str]
    username: str
    email: str
 


import models
from fastapi import FastAPI ,Request, Header,Form,Body,Path
from fastapi.templating import Jinja2Templates
from database import *
from enum import Enum
from pydantic import BaseModel,Field
from typing import Union,List


app = FastAPI()
#models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="Templates")
@app.get("/")
def dashboard(request: Request):

    return templates.TemplateResponse("Dashboard.html",{
        "request": request
    })


@app.get("/db")
def database():
    mycursor = conn.cursor()
    mycursor.execute('''select * from roles ''')
    myresult = mycursor.fetchall()
    print(myresult)

    return {
        "code": "success",
        "data": myresult
     }


# GET ROLES - *
@app.get("/api/roles")
async def getroles(Authorization:  Union[str, None] = Header(default=None), X_DeviceId: Union[str, None] = Header(default=None),
               X_Page: Union[str, None] = Header(default=None), X_Platform: Union[str, None] = Header(default=None),
               X_Product:Union[str, None] = Header(default=None), X_tenant:Union[str, None] = Header(default=None),
               isMultiSessionRequired: Union[bool, None] = Header(default=None)):


    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page": X_Page,
            "X_Platform": X_Platform,
            "X_Product": X_Product,
            "X_tenant": X_tenant,
            "isMultiSessionRequired": isMultiSessionRequired
            }




#CREATE ROLES
class Roles(BaseModel):
    displayname: str
    rolecode: str
    rolename: str

class RolesList(BaseModel):
    roles: List[Roles]


@app.post("/api/roles")
async def createroles(Authorization:  Union[str, None] = Header(default=None), X_DeviceId: Union[str, None] = Header(default=None),
               X_Page: Union[str, None] = Header(default=None), X_Platform: Union[str, None] = Header(default=None),
               X_Product:Union[str, None] = Header(default=None),X_tenant:Union[str, None] = Header(default=None),
               isMultiSessionRequired:Union[bool, None] = Header(default=None), roles: List[Roles] = Body(enable=True)):



    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired,
            "roles":roles
            }


#DELETE ROLES
@app.delete('/api/roles')
async def deleteroles(Authorization:  Union[str, None] = Header(default=None), X_DeviceId: Union[str, None] = Header(default=None),
               X_Page: Union[str, None] = Header(default=None), X_Platform: Union[str, None] = Header(default=None),X_Product:Union[str, None] = Header(default=None),
               X_tenant:Union[str, None] = Header(default=None), isMultiSessionRequired:Union[bool, None] = Header(default=None),
                role: List[int] = Body(embed=True)):

    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired,
            "role":role
            }

# UPDATE ROLES


@app.put("/api/roles/{role_id}")
async def updateRoles(Authorization:  Union[str, None] = Header(default=None), X_DeviceId: Union[str, None] = Header(default=None),
               X_Page: Union[str, None] = Header(default=None), X_Platform: Union[str, None] = Header(default=None),X_Product:Union[str, None] = Header(default=None),
               X_tenant:Union[str, None] = Header(default=None), isMultiSessionRequired:Union[bool, None] = Header(default=None), role_id: int = Path(title ="role_id"),
                active: Union[bool, None] = Body(embed=True),rolename: Union[str, None] = Body(embed= True)):


    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired,
            "role_id": role_id ,
            "active":active, "rolename":rolename
            }


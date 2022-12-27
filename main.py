import models
from fastapi import FastAPI ,Request, Header,Form,Body
from fastapi.templating import Jinja2Templates
from database import *
from enum import Enum
from pydantic import BaseModel
from typing import Union
#from database import SessionLocal,engine
#from sqlalchemy.orm import Session,engine
class ModelName(int, Enum):
    role_id = "role_id"


app = FastAPI()
#models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="Templates")
@app.get("/")
def dashboard(request: Request):
    """
    Displays the stock screener dashboard/homepage
    """
    return templates.TemplateResponse("Dashboard.html",{
        "request": request
    })


@app.get("/db")
def database():
    mycursor = conn.cursor()
    mycursor.execute('''select * from roles ''')
    myresult = mycursor.fetchall()
    print(myresult)
    #Avf_cart_value = pd.DataFrame(myresult)

    return {
        "code": "success",
        "data": myresult
     }

# GET ROLES
@app.get("/api/roles")
async def getroles(Authorization: str = Header(Default = None), X_DeviceId: str = Header(Default = None),
               X_Page: str = Header(Default = None), X_Platform: str = Header(Default = None),X_Product:str = Header(Default = None),
               X_tenant:str = Header(Default = None), isMultiSessionRequired: bool = Header(Default = None)):

    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired}


#CREATE ROLES

@app.post("/api/roles")
async def createroles(Authorization: str = Header(Default = None), X_DeviceId: str = Header(Default = None),
               X_Page: str = Header(Default = None), X_Platform: str = Header(Default = None),X_Product:str = Header(Default = None),
               X_tenant:str = Header(Default = None), isMultiSessionRequired: bool = Header(Default = None),
                displayname: str = Body(embed=True),rolecode : str = Body(embed=True), rolename: str = Body(embed=True)):


    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired, "displayname": displayname,"rolecode":rolecode,"rolename":rolename }



#DELETE ROLES
@app.delete('/api/roles')
async def deleteroles(Authorization: str = Header(Default = None), X_DeviceId: str = Header(Default = None),
               X_Page: str = Header(Default = None), X_Platform: str = Header(Default = None),X_Product:str = Header(Default = None),
               X_tenant:str = Header(Default = None), isMultiSessionRequired: bool = Header(Default = None),role: bool = Body(embed=True)):

    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired, "role":role}

# UPDATE ROLES

@app.put("/api/roles/{role_id}")
async def updateRoles(Authorization: str = Header(Default = None), X_DeviceId: str = Header(Default = None),
               X_Page: str = Header(Default = None), X_Platform: str = Header(Default = None),X_Product:str = Header(Default = None),
               X_tenant:str = Header(Default = None), isMultiSessionRequired: bool = Header(Default = None),role_id : ModelName,
                displayname: str = Body(embed=True),active : bool = Body(embed=True), rolename: str = Body(embed=True)):


    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page":X_Page,
            "X_Platform":X_Platform,
            "X_Product": X_Product,
            "X_tenant":X_tenant ,
            "isMultiSessionRequired":isMultiSessionRequired, "displayname": displayname,"active":active,"rolename":rolename,
            "role_id":role_id}


import models
from fastapi import FastAPI, Request, Header, Form, Body, HTTPException, Path
from fastapi.templating import Jinja2Templates
from database import *
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()
# models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="Templates")


@app.get("/")
def dashboard(request: Request):
    """
    Displays the stock screener dashboard/homepage
    """
    return templates.TemplateResponse("Dashboard.html", {
        "request": request
    })


@app.get("/api/health")
def database():
    mycursor = conn.cursor()
    mycursor.execute('''select * from roles ''')
    myresult = mycursor.fetchall()
    print(myresult)
    # Avf_cart_value = pd.DataFrame(myresult)

    return {
        "code": "success",
        "response": myresult
    }


# GET ROLES
@app.get("/api/roles")
async def getroles(Authorization: Union[str, None] = Header(default=None),
                   X_DeviceId: Union[str, None] = Header(default=None),
                   X_Page: Union[str, None] = Header(default=None), X_Platform: Union[str, None] = Header(default=None),
                   X_Product: Union[str, None] = Header(default=None),
                   X_tenant: Union[str, None] = Header(default=None),
                   isMultiSessionRequired: Union[bool, None] = Header(default=None)):
    mycursor = conn.cursor()
    mycursor.execute('''SELECT r.role_id,r.role_name,r.created_time,r.role_code,r.display_name,r.active
FROM roles r 
INNER JOIN tenant_roles tr 
ON r.role_id = tr.role_id AND tr.tenant_id = 1''')
    myresult = mycursor.fetchall()
    print(myresult)
    # Avf_cart_value = pd.DataFrame(myresult)

    return {
        # "code": "success",
        "response": myresult
    }


# CREATE ROLES

@app.post("/api/roles")
async def createroles(Authorization: Union[str, None] = Header(default=None),
                      X_DeviceId: Union[str, None] = Header(default=None),
                      X_Page: Union[str, None] = Header(default=None),
                      X_Platform: Union[str, None] = Header(default=None),
                      X_Product: Union[str, None] = Header(default=None),
                      X_tenant: Union[str, None] = Header(default=None),
                      isMultiSessionRequired: Union[bool, None] = Header(default=None),
                      displayname: Union[str, None] = Body(embed=True), rolecode: Union[str, None] = Body(embed=True),
                      rolename: Union[str, None] = Body(embed=True)):
    mycursor = conn.cursor()
    mycursor.execute(f"SELECT * FROM roles WHERE role_code='{rolecode}'")
    myresult = mycursor.fetchall()
    print(myresult)

    if myresult:
        print("true")
        raise HTTPException(
            status_code=400,
            detail=f"rolecode: {rolecode} already exist!"
        )
    else:
        print("false")
        query = f"INSERT INTO roles (role_name, active, role_code, display_name) VALUES ('{rolename}','1','{rolecode}','{displayname}')"
        myresult = mycursor.execute(query)
        myresult = mycursor.fetchall()
        print(myresult)

    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page": X_Page,
            "X_Platform": X_Platform,
            "X_Product": X_Product,
            "X_tenant": X_tenant,
            "isMultiSessionRequired": isMultiSessionRequired,
            "displayname": displayname,
            "rolecode": rolecode,
            "rolename": rolename
            }


# DELETE ROLES
@app.delete('/api/roles')
async def deleteroles(Authorization: Union[str, None] = Header(default=None),
                      X_DeviceId: Union[str, None] = Header(default=None),
                      X_Page: Union[str, None] = Header(default=None),
                      X_Platform: Union[str, None] = Header(default=None),
                      X_Product: Union[str, None] = Header(default=None),
                      X_tenant: Union[str, None] = Header(default=None),
                      isMultiSessionRequired: Union[bool, None] = Header(default=None),
                      role: Union[bool, None] = Body(embed=True)):
    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page": X_Page,
            "X_Platform": X_Platform,
            "X_Product": X_Product,
            "X_tenant": X_tenant,
            "isMultiSessionRequired": isMultiSessionRequired,
            "role": role
            }


# UPDATE ROLES

@app.put("/api/roles/{role_id}")
async def updateRoles(Authorization: Union[str, None] = Header(default=None),
                      X_DeviceId: Union[str, None] = Header(default=None),
                      X_Page: Union[str, None] = Header(default=None),
                      X_Platform: Union[str, None] = Header(default=None),
                      X_Product: Union[str, None] = Header(default=None),
                      X_tenant: Union[str, None] = Header(default=None),
                      isMultiSessionRequired: Union[bool, None] = Header(default=None),role_id: int = Path(title = "role_id"),
                      displayname: Union[str, None] = Body(embed=True), active: Union[int, None] = Body(embed=True),
                      rolename: Union[str, None] = Body(embed=True)):
    mycursor = conn.cursor()
    if rolename:
        mycursor.execute(f"UPDATE roles SET role_name='{rolename}' WHERE role_id = {role_id}")
        myresult = mycursor.fetchall()
        print(myresult)
    else:
        mycursor.execute(f"UPDATE roles SET ACTIVE='{active}' WHERE role_id = {role_id}")
        myresult = mycursor.fetchall()
        print(myresult)

    return {"Authorization values": Authorization,
            "X_DeviceId": X_DeviceId,
            "X_Page": X_Page,
            "X_Platform": X_Platform,
            "X_Product": X_Product,
            "X_tenant": X_tenant,
            "isMultiSessionRequired": isMultiSessionRequired, "displayname": displayname, "active": active,
            "rolename": rolename,
            "role_id": role_id
            }

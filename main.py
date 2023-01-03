import mysql.connector
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import datetime
from typing import Union,List
app = FastAPI()

# Database connection
from peewee import MySQLDatabase, Model, CharField

# Connect to the MySQL database
db = MySQLDatabase('infinitylearn', host='10.50.2.223', user='MatecharlaSreedharSanjana', password='cK592&TJw8ww')


# Data model
class Roles(BaseModel):
    displayName: str
    roleCode: str
    roleName: str

class updateRoles(BaseModel):
    active: int
    role_id: int
    roleName: str

# Create an item
@app.post("/api/role")
async def create_role(role: List[Roles]):
    cursor = db.cursor()

    for roleDetails in role:
        print(roleDetails.roleName)
        insert_query = f"INSERT INTO roles (role_name,active,role_code,display_name) VALUES ('{roleDetails.roleName}',1,'{roleDetails.roleCode}','{roleDetails.roleName}')"
        print(insert_query)
        #insert_query1 = f""
        result = cursor.execute(insert_query)
        result2 = db.commit()
        print(result)
        print(result2)
    cursor.close()
    return {"message":"success"}



# Read an item

@app.get("/api/roles")
async def read_role():
    cursor = db.cursor()
    select_query = "SELECT r.role_id,r.role_name,r.role_code FROM roles r INNER JOIN tenant_roles tr ON r.role_id = tr.role_id AND tr.tenant_id = 1"
    cursor.execute(select_query)
    item = cursor.fetchall()
    print(item)
    cursor.close()
    return {"response":item}

# Update an item
@app.put("/api/roles")
def update_role(role_id: int = Body(embed=True), active:int = Body(embed=True) , rolename : str = Body(embed=True)):
    cursor = db.cursor()
    print(role_id)
    if rolename != "":
        update_query = f"UPDATE roles SET role_name='{rolename}' WHERE role_id = {role_id}"
        print(update_query)
        myresult1 = cursor.execute(update_query)
        cursor.fetchall()
        db.commit()
        cursor.close()
        print(myresult1)
    else:
        update_query1 = f"UPDATE roles SET ACTIVE='{active}' WHERE role_id = {role_id}"
        print(update_query1)
        myresult = cursor.execute(update_query1)
        cursor.fetchall()
        db.commit()
        cursor.close()
        print(myresult)


    return {"message":"success"}

@app.put("/api/roles/test")
def update_role_test(role: updateRoles):
    cursor = db.cursor()
    print(role.role_id)
    # if role.rolename != "":
    update_query = f"UPDATE roles SET role_name='{role.rolename}' WHERE role_id = {role.role_id}"
    print(update_query)
    myresult1 = cursor.execute(update_query)
    cursor.fetchall()
    db.commit()
    cursor.close()
    print(myresult1)
    # else:
    #     update_query1 = f"UPDATE roles SET ACTIVE='{role.active}' WHERE role_id = {role.role_id}"
    #     print(update_query1)
    #     myresult = cursor.execute(update_query1)
    #     cursor.fetchall()
    #     db.commit()
    #     cursor.close()
    #     print(myresult)
    return {"status":"success"}

# Delete an item
@app.delete("/api/roles")
async def delete_role(role: List[Union[int, None]] = Body(embed=True)):
    cursor = db.cursor()

    for roleid in role:
        delete_query = f"DELETE FROM tenant_roles WHERE role_id IN ({roleid})"
        delete_query1 = f"DELETE FROM roles WHERE role_id IN ({roleid})"
        cursor.execute(delete_query)
        cursor.execute(delete_query1)
        db.commit()

    cursor.close()
    return {"status": "success"}

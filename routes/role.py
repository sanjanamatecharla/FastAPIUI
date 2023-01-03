from fastapi import APIRouter
from Config.database import conn
from models.index import roles
from Schemas.index import Role
role = APIRouter()

@role.get("/")
async def read_data():
    return conn.execute(Role.select()).fetchall()

@role.get("/{role_id}")
async def read_data(role_id:int):
    return conn.execute(Role.select().where (Role.c.code == role_id)).fetchall()

@role.post("/")
async def write_data(Role: roles):
    conn.execute(Role.insert().values(
        role_name = Role.name,
        active = Role.active,
    role_code= Role.role_code,
    display_name= Role.display_name
    ))
    return conn.execute(Role.select()).fetchall()

@role.put("/{role_id}")
async def update_data(role_id:int, Role: Role):
    conn.execute(Role.update().values(
        role_name=Role.name,
        active=Role.active,
        role_code=Role.role_code,
        display_name=Role.display_name
    ).where (Role.c.id == id))
    return conn.execute(Role.select()).fetchall()

@role.delete("/{role_id}")
async def delete_data(role_id:int):
    conn.execute(Role.delete().where(Role.c.id == id))
    return conn.execute(Role.select()).fetchall()

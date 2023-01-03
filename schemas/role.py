from pydantic import BaseModel

class Role(BaseModel):
    role_name: str
    active : int
    role_code: str
    display_name : str
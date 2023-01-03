from sqlalchemy import create_engine, Column, Integer, String,Sequence,DateTime,Boolean, Float

from database import Base
import datetime


class RolesModel(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String)
    role_code = Column(String)
    created_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, role_name: str, role_code: str):
        self.role_code = role_code
        self.role_name = role_name

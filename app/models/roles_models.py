from app.models import BaseModel
from sqlalchemy import Column, Integer, CHAR, Boolean


class RoleModel(BaseModel):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(CHAR(8))
    status = Column(Boolean, default=True)

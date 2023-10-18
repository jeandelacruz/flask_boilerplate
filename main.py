from app import app, db
from app import routers
from app.models import BaseModel
from app.utils import jwt


BaseModel.set_session(db.session)

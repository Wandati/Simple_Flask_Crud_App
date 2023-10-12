from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    description = db.Column(db.String(1000),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)

    
    def __repr__(self):
        return f"Task Name:{self.name}, Description: {self.description}"
    
    

#--- Importação da classe principal do alchemy
import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

# BaseAlchemy = declarative_base()
# class BaseModel(BaseAlchemy):
#     __tablename__ = "Produto"
#     def __init__(self):
#         self.db = db

BaseAlchemy = declarative_base()
class BaseModel(BaseAlchemy):
    __tablename__ ="endereco"
    def __init__(self):
        self.db = db

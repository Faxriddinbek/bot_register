import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from core.config import DB_USER, DB_NAME, DB_PORT, DB_PASS, DB_HOST
"""
bu o'zimning databaseimga ulanish
"""
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = databases.Database(DATABASE_URL) # databases librariy orqali ulanish (database.connect qilsa ulanadi)

"""
quyidagilar table yaratishda yordam beradi
"""
Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
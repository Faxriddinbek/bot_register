import sqlalchemy
from sqlalchemy import DateTime
# bu yerda model yasaladi
from core.database_settings import metadata# bu muhim

users = sqlalchemy.Table(
    "users",# bu databazadagi table nomi
    metadata,# bu muhim bo'lishi kerak
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("language", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.SmallInteger),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)
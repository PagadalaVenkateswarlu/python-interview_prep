from collections.abc import AsyncGenerator
import uuid
from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy import Column,String,Float,Text,Integer,ForeignKey,DateTime
from sqlalchemy.orm import DeclarativeBase,sessionmaker
import datetime
import os

import psycopg2

conn = psycopg2.connect(psycopg2.connect(
    host="db-prod.example.com",
    port=5432,
    database="ecommerce",
    user="admin"
))
cur = conn.cursor()
print(cur)

cur.execute("select * from users")
# print(cur.fetchall())
# print(cur.fetchone())
# print(cur.fetchmany())
# print(cur.rowcount)
# print(cur.description)
cur.close()
conn.close()


#
# DATABASE_URL = os.getenv("DATABASE_URL")
#
# engine = create_async_engine(DATABASE_URL)
# session = async_sessionmaker(engine,expire_on_commit=False)
#
# async def create_tables_db_conn():
#     async with engine.begin() as db_conn:
#         await db_conn.run_sync(DeclarativeBase.metadata.create_all)

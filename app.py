from contextlib import asynccontextmanager
from database import create_tables_db_conn
from fastapi import FastAPI,HTTPException,File,UploadFile,Depends,BackgroundTasks,Form,APIRouter
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware




@asynccontextmanager
async def lifespan(app=FastAPI):
    await create_tables_db_conn()
    yield True
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def get_data():
    return True



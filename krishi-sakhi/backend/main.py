import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_user, routes_farm, routes_activity, routes_advisory
from app.db.session import engine
from app.db.base import Base
load_dotenv()

# create DB tables (simple convenience for starter)
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Krishi Sakhi - Backend')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(routes_user.router, prefix='/api/users', tags=['users'])
app.include_router(routes_farm.router, prefix='/api/farms', tags=['farms'])
app.include_router(routes_activity.router, prefix='/api/activities', tags=['activities'])
app.include_router(routes_advisory.router, prefix='/api/advisory', tags=['advisory'])

@app.get('/ping')
def ping():
    return {'status':'ok'}

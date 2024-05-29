from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import get_db
from .functions import *
from .routes import dashboardRoutes, artistRoutes, albumRoutes, trackRoutes, playlistRoutes


# TODO add colaborative et datetime en bdd

app = FastAPI()

origins = ["*"]  # Allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboardRoutes.router)
app.include_router(artistRoutes.router)
app.include_router(albumRoutes.router)
app.include_router(trackRoutes.router)
app.include_router(playlistRoutes.router)

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import get_db
from .functions import *


app = FastAPI()

origins = ["*"]  # Allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/word-popularity")
def get_word_popularity_route(db: Session = Depends(get_db)):
    return get_playlist_name_popularity(db)


@app.get("/playlist-count")
def get_count_playlists_route(db: Session = Depends(get_db)):
    return get_number_of_playlists(db)


@app.get("/artist-count")
def get_count_artists_route(db: Session = Depends(get_db)):
    return get_number_of_artists(db)


@app.get("/track-count")
def get_count_tracks_route(db: Session = Depends(get_db)):
    return get_number_of_tracks(db)


@app.get("/album-count")
def get_count_albums_route(db: Session = Depends(get_db)):
    return get_number_of_albums(db)


@app.get("/artist-popularity")
def get_artist_popularity_route(db: Session = Depends(get_db)):
    return get_artist_popularity(db)


@app.get("/track-popularity")
def get_track_popularity_route(db: Session = Depends(get_db)):
    return get_track_popularity(db)

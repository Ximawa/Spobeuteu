from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.functions import *

router = APIRouter()


@router.get("/track-list/{track_name}")
def get_track_list_route(track_name: str, db: Session = Depends(get_db)):
    return get_track_starting_by(db, track_name)


@router.get("/track-popularity/{track_uri}")
def get_track_popularity_rank_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_popularity_rank(db, track_uri)


@router.get("/track-presence-playlists/{track_uri}")
def get_track_presence_playlists_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_presence_in_playlists(db, track_uri)


@router.get("/track-length/{track_uri}")
def get_track_length_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_length(db, track_uri)

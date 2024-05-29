from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.functions import *

router = APIRouter()


@router.get("/album-popularity/{album_uri}")
def get_album_popularity_rank_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_popularity_by_id(db, album_uri)


@router.get("/album-playlist-count/{album_uri}")
def get_album_playlist_count_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_presence_in_playlist(db, album_uri)


@router.get("/album-unique-tracks/{album_uri}")
def get_album_unique_tracks_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_unique_tracks_in_playlists(db, album_uri)


@router.get("/album-track-presence/{album_uri}")
def get_album_track_presence_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_tracks_in_playlists(db, album_uri)


@router.get("/track-popularity-by-album/{album_uri}")
def get_track_popularity_by_album_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_tracks_popularity(db, album_uri)


@router.get("/album-list/{album_name}")
def get_album_list_route(album_name: str, db: Session = Depends(get_db)):
    return get_album_starting_by(db, album_name)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.functions import *

router = APIRouter()


@router.get("/playlist-list/{playlist_name}")
def get_playlist_list_route(playlist_name: str, db: Session = Depends(get_db)):
    return get_playlist_starting_by(db, playlist_name)


@router.get("/playlist-track-count/{playlist_pid}")
def get_playlist_track_count_route(playlist_pid: str, db: Session = Depends(get_db)):
    return get_playlist_track_count(db, playlist_pid)


@router.get("/playlist-unique-artist-count/{playlist_pid}")
def get_playlist_unique_artist_count_route(playlist_pid: str, db: Session = Depends(get_db)):
    return get_playlist_unique_artist_count(db, playlist_pid)


@router.get("/playlist-unique-album-count/{playlist_pid}")
def get_playlist_unique_album_count_route(playlist_pid: str, db: Session = Depends(get_db)):
    return get_playlist_unique_album_count(db, playlist_pid)


@router.get("/playlist-avg-track-duration/{playlist_pid}")
def get_playlist_avg_track_duration_route(playlist_pid: str, db: Session = Depends(get_db)):
    return get_playlist_avg_track_duration(db, playlist_pid)


@router.get("/playlist-artist-track-count/{playlist_pid}")
def get_playlist_artist_track_count_route(playlist_pid: str, db: Session = Depends(get_db)):
    return get_playlist_artist_track_count(db, playlist_pid)

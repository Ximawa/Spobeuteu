from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.functions import *

router = APIRouter()


@router.get("/artist-popularity")
def get_artist_popularity_route(db: Session = Depends(get_db)):
    return get_artist_popularity(db)


@router.get("/word-popularity")
def get_word_popularity_route(db: Session = Depends(get_db)):
    return get_playlist_name_popularity(db)


@router.get("/track-popularity")
def get_track_popularity_route(db: Session = Depends(get_db)):
    return get_track_popularity(db)


@router.get("/average-tracks-length")
def get_average_tracks_length_route(db: Session = Depends(get_db)):
    return get_average_tracks_length(db)


@router.get("/album-popularity")
def get_album_popularity_route(db: Session = Depends(get_db)):
    return get_album_popularity(db)


@router.get("/playlist-count")
def get_count_playlists_route(db: Session = Depends(get_db)):
    return get_number_of_playlists(db)


@router.get("/track-count")
def get_count_tracks_route(db: Session = Depends(get_db)):
    return get_number_of_tracks(db)


@router.get("/artist-count")
def get_count_artists_route(db: Session = Depends(get_db)):
    return get_number_of_artists(db)


@router.get("/album-count")
def get_count_albums_route(db: Session = Depends(get_db)):
    return get_number_of_albums(db)

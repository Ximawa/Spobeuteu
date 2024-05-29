from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.functions import *

router = APIRouter()


@router.get("/playlist-count/{artist_uri}")
def get_artist_playlist_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_presence_in_playlists(db, artist_uri)


@router.get("/track-count/{artist_uri}")
def get_artist_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_tracks_count_in_playlist(db, artist_uri)


@router.get("/album-count/{artist_uri}")
def get_artist_album_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_albums_in_playlists(db, artist_uri)


@router.get("/artist-popularity/{artist_uri}")
def get_artist_popularity_rank_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_popularity_rank(db, artist_uri)


@router.get("/artist-tracks-popularity/{artist_uri}")
def get_artist_tracks_popularity_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_track_popularity_by_artist(db, artist_uri)


@router.get("/artist-album-popularity/{artist_uri}")
def get_artist_album_popularity_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_album_popularity_by_artist(db, artist_uri)


@router.get("/artist-list/{artist_name}")
def get_artist_list_route(artist_name: str, db: Session = Depends(get_db)):
    return get_artist_starting_by(db, artist_name)

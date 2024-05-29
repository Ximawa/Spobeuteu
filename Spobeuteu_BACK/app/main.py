from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import get_db
from .functions import *

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


@app.get("/album-popularity")
def get_album_popularity_route(db: Session = Depends(get_db)):
    return get_album_popularity(db)


@app.get("/average-tracks-length")
def get_average_tracks_length_route(db: Session = Depends(get_db)):
    return get_average_tracks_length(db)


@app.get("/artist-list/{artist_name}")
def get_artist_list_route(artist_name: str, db: Session = Depends(get_db)):
    return get_artist_starting_by(db, artist_name)


@app.get("/album-list/{album_name}")
def get_album_list_route(album_name: str, db: Session = Depends(get_db)):
    return get_album_starting_by(db, album_name)


@app.get("/track-list/{track_name}")
def get_track_list_route(track_name: str, db: Session = Depends(get_db)):
    return get_track_starting_by(db, track_name)


@app.get("/track-count/{artist_uri}")
def get_artist_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_tracks_count_in_playlist(db, artist_uri)


@app.get("/playlist-count/{artist_uri}")
def get_artist_playlist_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_presence_in_playlists(db, artist_uri)


@app.get("/album-count/{artist_uri}")
def get_artist_album_count_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_albums_in_playlists(db, artist_uri)


@app.get("/artist-popularity/{artist_uri}")
def get_artist_popularity_rank_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_artist_popularity_rank(db, artist_uri)


@app.get("/artist-tracks-popularity/{artist_uri}")
def get_artist_tracks_popularity_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_track_popularity_by_artist(db, artist_uri)


@app.get("/artist-album-popularity/{artist_uri}")
def get_artist_album_popularity_route(artist_uri: str, db: Session = Depends(get_db)):
    return get_album_popularity_by_artist(db, artist_uri)


@app.get("/album-popularity/{album_uri}")
def get_album_popularity_rank_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_popularity_by_id(db, album_uri)


@app.get("/album-playlist-count/{album_uri}")
def get_album_playlist_count_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_presence_in_playlist(db, album_uri)


@app.get("/album-unique-tracks/{album_uri}")
def get_album_unique_tracks_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_unique_tracks_in_playlists(db, album_uri)


@app.get("/album-track-presence/{album_uri}")
def get_album_track_presence_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_tracks_in_playlists(db, album_uri)


@app.get("/track-popularity-by-album/{album_uri}")
def get_track_popularity_by_album_route(album_uri: str, db: Session = Depends(get_db)):
    return get_album_tracks_popularity(db, album_uri)


@app.get("/track-popularity/{track_uri}")
def get_track_popularity_rank_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_popularity_rank(db, track_uri)


@app.get("/track-presence-playlists/{track_uri}")
def get_track_presence_playlists_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_presence_in_playlists(db, track_uri)


@app.get("/track-length/{track_uri}")
def get_track_length_route(track_uri: str, db: Session = Depends(get_db)):
    return get_track_length(db, track_uri)

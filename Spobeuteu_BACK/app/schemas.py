from pydantic import BaseModel
from typing import List


class Artist(BaseModel):
    artist_uri: str
    artist_name: str

    class Config:
        orm_mode = True


class Album(BaseModel):
    album_uri: str
    album_name: str
    artist_uri: str

    class Config:
        orm_mode = True


class Track(BaseModel):
    track_uri: str
    track_name: str
    duration_ms: int
    artist_uri: str
    album_uri: str

    class Config:
        orm_mode = True


class Playlist(BaseModel):
    pid: str
    name: str
    collaborative: bool
    modified_at: str
    num_followers: int
    num_tracks: int
    num_albums: int

    class Config:
        orm_mode = True


class ChartData(BaseModel):
    labels: List[str]
    data: List[int]

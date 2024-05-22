from sqlalchemy import Column,  ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# Créer une instance de Base
Base = declarative_base()


class Track(Base):
    __tablename__ = 'tracks'

    track_uri = Column(String(250), primary_key=True)
    track_name = Column(String(250))
    duration_ms = Column(Integer)
    artist_uri = Column(String(250), ForeignKey('artists.artist_uri'))
    album_uri = Column(String(250), ForeignKey('albums.album_uri'))

    artist = relationship("Artist", back_populates="track")
    album = relationship("Album", back_populates="track")
    playlist = relationship("PlaylistTrack", back_populates="track")

    def __repr__(self):
        return f"<Track(track_uri='{self.track_uri}', track_name='{self.track_name}', duration_ms='{self.duration_ms}')>"


class Artist(Base):
    __tablename__ = 'artists'

    artist_uri = Column(String(250), primary_key=True)
    artist_name = Column(String(250))

    album = relationship("Album", back_populates="artist")
    track = relationship("Track", back_populates="artist")

    def __repr__(self):
        return f"<Artist(artist_uri='{self.artist_uri}', artist_name='{self.artist_name}')>"


class Album(Base):
    __tablename__ = 'albums'

    album_uri = Column(String(250), primary_key=True)
    album_name = Column(String(250))
    artist_uri = Column(String(250), ForeignKey('artists.artist_uri'))

    artist = relationship("Artist", back_populates="album")
    track = relationship("Track", back_populates="album")

    def __repr__(self):
        return f"<Album(album_uri='{self.album_uri}', album_name='{self.album_name}', artist_uri='{self.artist_uri}')>"


class Playlist(Base):
    __tablename__ = 'playlists'

    # TODO: corriger collaborative et modified_at
    pid = Column(String(250), primary_key=True)
    name = Column(String(250))
    collaborative = Column(Boolean, default=False)
    modified_at = Column(DateTime, default=None)
    num_followers = Column(Integer)
    num_tracks = Column(Integer)
    num_albums = Column(Integer)

    track = relationship("PlaylistTrack", back_populates="playlist")

    def __repr__(self):
        return f"<Playlist(pid='{self.pid}', playlist_name='{self.playlist_name}', collaborative='{self.collaborative}', modified_at='{self.modified_at}', num_followers='{self.num_followers}', num_tracks='{self.num_tracks}', num_albums='{self.num_albums}')>"


class PlaylistTrack(Base):
    __tablename__ = 'playlist_tracks'

    id = Column(Integer, primary_key=True, autoincrement=True)

    pid = Column(String(100), ForeignKey('playlists.pid'))
    track_uri = Column(String(100), ForeignKey('tracks.track_uri'))
    pos = Column(Integer)

    playlist = relationship("Playlist", back_populates="track")
    track = relationship("Track", back_populates="playlist")

    def __repr__(self):
        return f"<PlaylistTrack(pid='{self.pid}', track_uri='{self.track_uri}', pos='{self.pos}')>"


def get_engine():
    username = "root"
    password = ""
    database_name = "spobeuteu"

    database_url = f"mysql+pymysql://{
        username}:{password}@localhost/{database_name}"
    return create_engine(database_url)


def create_tables(engine):
    Base.metadata.create_all(engine)


def main():
    engine = get_engine()
    create_tables(engine)
    print("Tables created successfully")


if __name__ == "__main__":
    main()

from sqlalchemy.orm import Session
from .models import Playlist, Artist, Track, Album
from sqlalchemy.orm import Session
from sqlalchemy import func


def get_word_popularity(playlists, limit):
    word_popularity = {}
    for playlist in playlists:
        words = playlist.name.split()
        for word in words:
            if word in word_popularity:
                word_popularity[word] += 1
            else:
                word_popularity[word] = 1

    # Convert the word_popularity dictionary to the desired format
    word_popularity_list = [{"text": word, "value": count}
                            for word, count in word_popularity.items()]

    # Sort the list in descending order of popularity
    word_popularity_list.sort(key=lambda x: x['value'], reverse=True)

    return word_popularity_list[:limit]


def get_all_playlists_names(db: Session):
    return db.query(Playlist.name).all()


def get_playlist_name_popularity(db: Session):
    playlists = get_all_playlists_names(db)
    return get_word_popularity(playlists, 100)


def get_number_of_playlists(db: Session):
    return db.query(Playlist).count()


def get_number_of_artists(db: Session):
    return db.query(Artist).count()


def get_number_of_tracks(db: Session):
    return db.query(Track).count()


def get_number_of_albums(db: Session):
    return db.query(Album).count()


def get_artist_popularity(db: Session):
    # Query for artist popularity in a single query
    artist_popularity_list = db.query(Artist.artist_name, func.count(Track.artist_uri).label('count')).join(
        Track, Track.artist_uri == Artist.artist_uri).group_by(Artist.artist_name).order_by(func.count(Track.artist_uri).desc()).limit(10).all()

    # Convert the result to the desired format
    artist_popularity_list = [{"text": name, "value": count}
                              for name, count in artist_popularity_list]

    return artist_popularity_list


# TODO add nom de l'artist des chanson
def get_track_popularity(db: Session):
    # Query for track popularity in a single query
    track_popularity_list = db.query(Track.track_name + " by " + Artist.artist_name, func.count(Track.track_uri).label(
        'count')).join(Artist, Artist.artist_uri == Track.artist_uri).group_by(Track.track_name).order_by(func.count(Track.track_uri).desc()).limit(10).all()

    # Convert the result to the desired format
    track_popularity_list = [{"text": name, "value": count}
                             for name, count in track_popularity_list]

    return track_popularity_list

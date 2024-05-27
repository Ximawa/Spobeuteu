from sqlalchemy.orm import Session
from .models import Playlist, Artist, Track, Album


def get_word_popularity(playlists):
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
    return word_popularity_list


def get_all_playlists_names(db: Session):
    return db.query(Playlist.name).all()


def get_playlist_name_popularity(db: Session):
    playlists = get_all_playlists_names(db)
    return get_word_popularity(playlists)


def get_number_of_playlists(db: Session):
    return db.query(Playlist).count()


def get_number_of_artists(db: Session):
    return db.query(Artist).count()


def get_number_of_tracks(db: Session):
    return db.query(Track).count()


def get_number_of_albums(db: Session):
    return db.query(Album).count()

from sqlalchemy.orm import Session
from .models import Playlist, Artist, Track, Album, PlaylistTrack
from sqlalchemy.orm import Session
from sqlalchemy import func, text


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
    artist_popularity_list = db.query(
        Artist.artist_name,
        func.count(PlaylistTrack.pid).label('count')
    ).select_from(
        Artist
    ).join(
        Track, Track.artist_uri == Artist.artist_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Artist.artist_name
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).limit(10).all()

    # Convert the result to the desired format
    artist_popularity_list = [{"text": name, "value": count}
                              for name, count in artist_popularity_list]

    return artist_popularity_list


def get_track_popularity(db: Session):
    # Query for track popularity in a single query
    track_popularity_list = db.query(
        Track.track_name + " by " + Artist.artist_name,
        func.count(PlaylistTrack.pid).label('count')
    ).select_from(
        Track
    ).join(
        Artist, Artist.artist_uri == Track.artist_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Track.track_name, Artist.artist_name
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).limit(10).all()

    # Convert the result to the desired format
    track_popularity_list = [{"text": name, "value": count}
                             for name, count in track_popularity_list]

    return track_popularity_list


def get_album_popularity(db: Session):
    # Query for all albums ordered by popularity
    album_popularity_list = db.query(
        Album.album_name,
        func.count(PlaylistTrack.pid).label('count')
    ).select_from(
        Album
    ).join(
        Track, Track.album_uri == Album.album_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Album.album_name
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).limit(10).all()

    # Convert the result to the desired format
    album_popularity_list = [{"text": name, "value": count}
                             for name, count in album_popularity_list]

    return album_popularity_list


def get_average_tracks_length(db: Session):
    # Query for track duration in 15 seconds intervals
    track_duration_list = db.query(
        (func.round(Track.duration_ms / 15000) * 15).label('interval'),
        func.count(Track.track_uri).label('count')
    ).group_by('interval').all()

    # Convert the result to the desired format
    track_duration_list = [{
        "text": f"{int(interval // 60)}:{int(interval % 60):02d}",
        "value": count
    } for interval, count in track_duration_list]

    return track_duration_list


def get_artist_starting_by(db: Session, letter: str):
    # Query for artist URIs and names starting with the given letter
    artist_list = db.query(Artist.artist_uri, Artist.artist_name).filter(
        Artist.artist_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the artist URIs and the values are the artist names
    artist_dict = {uri: name for uri, name in artist_list}

    return artist_dict


def get_artist_tracks_count_in_playlist(db: Session, artist_uri: str):
    # Query for the count of tracks by the given artist in a single query
    count = db.query(func.count(Track.track_name)).filter(
        Track.artist_uri == artist_uri).scalar()

    return count


def get_artist_presence_in_playlists(db: Session, artist_uri: str):
   # Query for the count of distinct playlists that contain a track by the given artist
    count = db.query(PlaylistTrack.pid).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.artist_uri == artist_uri
    ).distinct().count()

    return count


def get_artist_albums_in_playlists(db: Session, artist_uri: str):
    # Query for the count of distinct albums of the given artist that are in playlists
    count = db.query(Album.album_uri).join(
        Track, Track.album_uri == Album.album_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        Track.artist_uri == artist_uri
    ).distinct().count()

    return count


def get_artist_popularity_rank(db: Session, artist_uri: str):
    # Subquery to count the number of tracks by each artist in playlists
    subquery = db.query(
        Track.artist_uri,
        func.count(PlaylistTrack.pid).label('popularity')
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Track.artist_uri
    ).subquery()

    # Query to get the popularity of the given artist
    artist_popularity = db.query(
        subquery.c.popularity
    ).filter(
        subquery.c.artist_uri == artist_uri
    ).scalar()

    # Query to get the rank of the given artist in the popularity ladder
    rank = db.query(
        func.count(subquery.c.artist_uri)
    ).filter(
        subquery.c.popularity > artist_popularity
    ).scalar()

    # Add 1 to the rank because the rank is 0-based
    rank += 1

    return rank


def get_track_popularity_by_artist(db: Session, artist_uri: str):
    # Query for track popularity by the given artist in a single query
    track_popularity_list = db.query(
        Track.track_name,
        func.count(PlaylistTrack.pid).label('count')
    ).join(
        Artist, Artist.artist_uri == Track.artist_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        Artist.artist_uri == artist_uri
    ).group_by(
        Track.track_name
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).limit(10).all()

    # Convert the result to the desired format
    track_popularity_list = [{"text": name, "value": count}
                             for name, count in track_popularity_list]

    return track_popularity_list


def get_album_popularity_by_artist(db: Session, artist_uri: str):
    # Query for album popularity by the given artist in a single query
    album_popularity_list = db.query(
        Album.album_name,
        func.count(PlaylistTrack.pid).label('count')
    ).select_from(
        Album
    ).join(
        Track, Track.album_uri == Album.album_uri
    ).join(
        Artist, Artist.artist_uri == Track.artist_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        Artist.artist_uri == artist_uri
    ).group_by(
        Album.album_name
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).limit(10).all()

    # Convert the result to the desired format
    album_popularity_list = [{"text": name, "value": count}
                             for name, count in album_popularity_list]

    return album_popularity_list


def get_album_popularity_by_id(db: Session, album_uri: str):
    # Query for all albums ordered by popularity
    album_popularity_list = db.query(
        Album.album_uri,
        func.count(PlaylistTrack.pid).label('count')
    ).select_from(
        Album
    ).join(
        Track, Track.album_uri == Album.album_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Album.album_uri
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).all()

    # Create a dictionary with album_uri as key and its rank as value
    album_rank_dict = {uri: rank+1 for rank,
                       (uri, _) in enumerate(album_popularity_list)}

    # Get the rank of the given album
    album_rank = album_rank_dict.get(
        album_uri, "Album not found in the popularity list.")

    return album_rank


def get_album_starting_by(db: Session, letter: str):
    # Query for album URIs and names starting with the given letter
    album_list = db.query(Album.album_uri, Album.album_name).filter(
        Album.album_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the album URIs and the values are the album names
    album_dict = {uri: name for uri, name in album_list}

    return album_dict


def get_album_presence_in_playlist(db: Session, album_uri: str):
    # Query for the count of distinct playlists that contain a track from the given album
    count = db.query(PlaylistTrack.pid).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).distinct().count()

    return count


def get_album_unique_tracks_in_playlists(db: Session, album_uri: str):
    # Query for the count of distinct tracks from the given album that appear in any playlist
    count = db.query(PlaylistTrack.track_uri).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).distinct().count()

    return count


def get_album_tracks_in_playlists(db: Session, album_uri: str):
    # Query for the count of all instances where a track from the given album appears in a playlist
    count = db.query(PlaylistTrack).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).count()

    return count


def get_album_tracks_popularity(db: Session, album_uri: str):
    # Query for each track in the given album and its popularity
    tracks_popularity = db.query(
        Track.track_name,
        func.count(PlaylistTrack.pid).label('value')
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).group_by(
        Track.track_name
    ).all()

    # Convert the result to the desired format
    tracks_popularity = [{"text": name, "value": value}
                         for name, value in tracks_popularity]

    return tracks_popularity


def get_track_starting_by(db: Session, letter: str):
    # Query for track URIs and names starting with the given letter
    track_list = db.query(Track.track_uri, Track.track_name).filter(
        Track.track_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the track URIs and the values are the track names
    track_dict = {uri: name for uri, name in track_list}

    return track_dict


def get_track_popularity_rank(db: Session, track_uri: str):
    # Query for all tracks and their popularity
    tracks_popularity = db.query(
        Track.track_uri,
        func.count(PlaylistTrack.pid).label('popularity')
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).group_by(
        Track.track_uri
    ).order_by(
        func.count(PlaylistTrack.pid).desc()
    ).all()

    # Create a dictionary with track_uri as key and its rank as value
    track_rank_dict = {uri: rank+1 for rank,
                       (uri, _) in enumerate(tracks_popularity)}

    # Get the rank of the given track
    track_rank = track_rank_dict.get(
        track_uri, "Track not found in the popularity list.")

    return track_rank


def get_track_presence_in_playlists(db: Session, track_uri: str):
    # Query for the count of playlists that contain the given track
    count = db.query(PlaylistTrack.pid).filter(
        PlaylistTrack.track_uri == track_uri
    ).distinct().count()

    return count


def get_track_length(db: Session, track_uri: str):
    # Query for the length of the given track
    track_length = db.query(Track.duration_ms).filter(
        Track.track_uri == track_uri
    ).first()

    if track_length is None:
        return "Track not found."

    # Convert the length to seconds
    track_length_in_seconds = track_length[0] / 1000

    return track_length_in_seconds

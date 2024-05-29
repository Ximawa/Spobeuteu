from sqlalchemy.orm import Session
from .models import Playlist, Artist, Track, Album, PlaylistTrack
from sqlalchemy.orm import Session
from sqlalchemy import func


def get_word_popularity(playlists, limit):
    """
    Calculates the popularity of words in a list of playlists.

    Args:
        playlists (list): A list of playlists.
        limit (int): The maximum number of popular words to return.

    Returns:
        list: A list of dictionaries containing the popular words and their counts,
              sorted in descending order of popularity.
    """
    # Create a dictionary to store the word popularity
    word_popularity = {}

    # Iterate over each playlist
    for playlist in playlists:
        # Split the playlist name into words
        words = playlist.name.split()

        # Count the occurrence of each word
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

    # Return the top 'limit' popular words
    return word_popularity_list[:limit]


def get_all_playlists_names(db: Session):
    """
    Retrieves the names of all playlists from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[str]: A list of playlist names.
    """
    # Query the database to retrieve all playlist names
    return db.query(Playlist.name).all()


def get_playlist_name_popularity(db: Session):
    """
    Retrieves all playlist names from the database and calculates the popularity of each name.

    Args:
        db (Session): The database session object.

    Returns:
        dict: A dictionary containing the playlist names as keys and their popularity as values.
    """
    playlists = get_all_playlists_names(db)
    return get_word_popularity(playlists, 100)


def get_number_of_playlists(db: Session):
    """
    Returns the number of playlists in the database.

    Parameters:
    - db: The database session.

    Returns:
    - The number of playlists in the database.
    """
    # Count the number of playlists in the database
    return db.query(Playlist).count()


def get_number_of_artists(db: Session):
    """
    Returns the number of artists in the database.

    Parameters:
    - db (Session): The database session.

    Returns:
    - int: The number of artists in the database.
    """
    # Count the number of artists in the database
    return db.query(Artist).count()


def get_number_of_tracks(db: Session):
    """
    Returns the number of tracks in the database.

    Parameters:
    - db: The database session.

    Returns:
    - The number of tracks in the database.
    """
    # Count the number of tracks in the database
    return db.query(Track).count()


def get_number_of_albums(db: Session):
    """
    Returns the number of albums in the database.

    Parameters:
    - db: The database session.

    Returns:
    - The number of albums in the database.
    """
    return db.query(Album).count()  # Count the number of albums in the database


def get_artist_popularity(db: Session):
    """
    Retrieves the popularity of artists based on the number of times their tracks appear in playlists.

    Args:
        db (Session): The database session object.

    Returns:
        list: A list of dictionaries containing the artist name and the count of their tracks in playlists.
    """
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
    """
    Retrieves the popularity of tracks based on the number of times they appear in playlists.

    Args:
        db (Session): The database session object.

    Returns:
        list: A list of dictionaries containing the track name and its popularity count.
              Each dictionary has the following structure: {"text": track_name, "value": popularity_count}
    """

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
    """
    Retrieves the popularity of albums based on the number of times they appear in playlists.

    Args:
        db (Session): The database session object.

    Returns:
        list: A list of dictionaries containing the album name and its popularity count.
              Each dictionary has the keys 'text' and 'value'.
    """
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
    """
    Retrieves the average length of tracks in 15 seconds intervals from the database.

    Args:
        db (Session): The database session object.

    Returns:
        list: A list of dictionaries containing the interval and count of tracks in that interval.
              Each dictionary has a "text" key representing the interval in minutes and seconds,
              and a "value" key representing the count of tracks in that interval.
    """
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
    """
    Retrieve a dictionary of artist URIs and names starting with the given letter.

    Args:
        db (Session): The database session.
        letter (str): The starting letter.

    Returns:
        dict: A dictionary where the keys are the artist URIs and the values are the artist names.
    """
    # Query for artist URIs and names starting with the given letter
    artist_list = db.query(Artist.artist_uri, Artist.artist_name).filter(
        Artist.artist_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the artist URIs and the values are the artist names
    artist_dict = {uri: name for uri, name in artist_list}

    return artist_dict


def get_artist_tracks_count_in_playlist(db: Session, artist_uri: str):
    """
    Retrieves the count of tracks by the given artist in a playlist.

    Args:
        db (Session): The database session.
        artist_uri (str): The URI of the artist.

    Returns:
        int: The count of tracks by the artist in the playlist.
    """
    count = db.query(func.count(Track.track_name)).filter(
        Track.artist_uri == artist_uri).scalar()

    return count


def get_artist_presence_in_playlists(db: Session, artist_uri: str):
    """
    Retrieves the count of distinct playlists that contain a track by the given artist.

    Args:
        db (Session): The database session.
        artist_uri (str): The URI of the artist.

    Returns:
        int: The count of distinct playlists.
    """
    # Query for the count of distinct playlists that contain a track by the given artist
    count = db.query(PlaylistTrack.pid).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.artist_uri == artist_uri
    ).distinct().count()

    return count


def get_artist_albums_in_playlists(db: Session, artist_uri: str):
    """
    Retrieves the count of distinct albums of the given artist that are present in playlists.

    Args:
        db (Session): The database session object.
        artist_uri (str): The URI of the artist.

    Returns:
        int: The count of distinct albums of the given artist in playlists.
    """
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
    """
    Retrieves the popularity rank of a given artist based on the number of tracks in playlists.

    Args:
        db (Session): The database session object.
        artist_uri (str): The URI of the artist.

    Returns:
        int: The popularity rank of the artist.
    """
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
    """
    Retrieves the track popularity by the given artist.

    Args:
        db (Session): The database session.
        artist_uri (str): The URI of the artist.

    Returns:
        list: A list of dictionaries containing the track name and its popularity count.
    """
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
    """
    Retrieves the popularity of albums by a given artist.

    Args:
        db (Session): The database session object.
        artist_uri (str): The URI of the artist.

    Returns:
        list: A list of dictionaries containing the album name and its popularity count.
              Each dictionary has the following structure: {"text": album_name, "value": popularity_count}.
    """
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
    """
    Retrieves the popularity rank of an album based on the number of times its tracks appear in playlists.

    Args:
        db (Session): The database session object.
        album_uri (str): The URI of the album.

    Returns:
        int: The popularity rank of the album. Returns "Album not found in the popularity list." if the album is not found.
    """
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
    """
    Retrieve a dictionary of album URIs and names starting with the given letter.

    Args:
        db (Session): The database session.
        letter (str): The starting letter.

    Returns:
        dict: A dictionary where the keys are the album URIs and the values are the album names.
    """
    # Query for album URIs and names starting with the given letter
    album_list = db.query(Album.album_uri, Album.album_name).filter(
        Album.album_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the album URIs and the values are the album names
    album_dict = {uri: name for uri, name in album_list}

    return album_dict


def get_album_presence_in_playlist(db: Session, album_uri: str):
    """
    Retrieves the count of distinct playlists that contain a track from the given album.

    Args:
        db (Session): The database session object.
        album_uri (str): The URI of the album.

    Returns:
        int: The count of distinct playlists that contain a track from the given album.
    """
    # Query for the count of distinct playlists that contain a track from the given album
    count = db.query(PlaylistTrack.pid).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).distinct().count()

    return count


def get_album_unique_tracks_in_playlists(db: Session, album_uri: str):
    """
    Retrieves the count of distinct tracks from the given album that appear in any playlist.

    Args:
        db (Session): The database session object.
        album_uri (str): The URI of the album.

    Returns:
        int: The count of distinct tracks from the album that appear in any playlist.
    """
    # Query for the count of distinct tracks from the given album that appear in any playlist
    count = db.query(PlaylistTrack.track_uri).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).distinct().count()

    return count


def get_album_tracks_in_playlists(db: Session, album_uri: str):
    """
    Retrieves the count of all instances where a track from the given album appears in a playlist.

    Args:
        db (Session): The database session.
        album_uri (str): The URI of the album.

    Returns:
        int: The count of instances where a track from the album appears in a playlist.
    """
    # Query for the count of all instances where a track from the given album appears in a playlist
    count = db.query(PlaylistTrack).join(
        Track, Track.track_uri == PlaylistTrack.track_uri
    ).filter(
        Track.album_uri == album_uri
    ).count()

    return count


def get_album_tracks_popularity(db: Session, album_uri: str):
    """
    Retrieves the popularity of each track in a given album.

    Args:
        db (Session): The database session.
        album_uri (str): The URI of the album.

    Returns:
        List[Dict[str, Union[str, int]]]: A list of dictionaries containing the track name and its popularity value.
    """
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
    """
    Retrieve a dictionary of track URIs and names starting with the given letter.

    Args:
        db (Session): The database session.
        letter (str): The starting letter.

    Returns:
        dict: A dictionary where the keys are the track URIs and the values are the track names.
    """
    # Query for track URIs and names starting with the given letter
    track_list = db.query(Track.track_uri, Track.track_name).filter(
        Track.track_name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the track URIs and the values are the track names
    track_dict = {uri: name for uri, name in track_list}

    return track_dict


def get_track_popularity_rank(db: Session, track_uri: str):
    """
    Retrieves the popularity rank of a given track based on the number of times it appears in playlists.

    Args:
        db (Session): The database session object.
        track_uri (str): The URI of the track.

    Returns:
        int: The popularity rank of the track. Returns "Track not found in the popularity list." if the track is not found.
    """
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
    """
    Retrieves the count of playlists that contain a given track.

    Args:
        db (Session): The database session.
        track_uri (str): The URI of the track.

    Returns:
        int: The count of playlists that contain the track.
    """
    # Query for the count of playlists that contain the given track
    count = db.query(PlaylistTrack.pid).filter(
        PlaylistTrack.track_uri == track_uri
    ).distinct().count()

    return count


def get_track_length(db: Session, track_uri: str):
    """
    Retrieves the length of a track from the database.

    Args:
        db (Session): The database session.
        track_uri (str): The URI of the track.

    Returns:
        float: The length of the track in seconds, or "Track not found." if the track is not found.
    """
    # Query for the length of the given track
    track_length = db.query(Track.duration_ms).filter(
        Track.track_uri == track_uri
    ).first()

    if track_length is None:
        return "Track not found."

    # Convert the length to seconds
    track_length_in_seconds = track_length[0] / 1000

    return track_length_in_seconds


def get_playlist_starting_by(db: Session, letter: str):
    """
    Retrieve a dictionary of playlist URIs and names starting with the given letter.

    Args:
        db (Session): The database session.
        letter (str): The starting letter.

    Returns:
        dict: A dictionary where the keys are the playlist URIs and the values are the playlist names.
    """
    # Query for playlist URIs and names starting with the given letter
    playlist_list = db.query(Playlist.pid, Playlist.name).filter(
        Playlist.name.like(f'{letter}%')).all()

    # Create a dictionary where the keys are the playlist URIs and the values are the playlist names
    playlist_dict = {pid: name for pid, name in playlist_list}

    return playlist_dict


def get_playlist_track_count(db: Session, playlist_pid: str):
    """
    Retrieves the count of tracks in the given playlist.

    Args:
        db (Session): The database session.
        playlist_pid (str): The playlist PID.

    Returns:
        int: The count of tracks in the playlist.
    """
    # Query for the count of tracks in the given playlist
    count = db.query(PlaylistTrack.track_uri).filter(
        PlaylistTrack.pid == playlist_pid
    ).count()

    return count


def get_playlist_unique_artist_count(db: Session, playlist_pid: str):
    """
    Retrieves the count of unique artists in a given playlist.

    Args:
        db (Session): The database session.
        playlist_pid (str): The playlist PID.

    Returns:
        int: The count of distinct artists in the playlist.
    """
    # Query for the count of distinct artists in the given playlist
    count = db.query(Track.artist_uri).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        PlaylistTrack.pid == playlist_pid
    ).distinct().count()

    return count


def get_playlist_unique_album_count(db: Session, playlist_pid: str):
    """
    Retrieves the count of distinct albums in the given playlist.

    Args:
        db (Session): The database session.
        playlist_pid (str): The playlist PID.

    Returns:
        int: The count of distinct albums in the playlist.
    """
    # Query for the count of distinct albums in the given playlist
    count = db.query(Track.album_uri).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        PlaylistTrack.pid == playlist_pid
    ).distinct().count()

    return count


def get_playlist_avg_track_duration(db: Session, playlist_pid: str):
    """
    Calculate the average duration of tracks in a given playlist.

    Args:
        db (Session): The database session.
        playlist_pid (str): The playlist PID.

    Returns:
        float: The average duration of tracks in seconds, or "No tracks found in the playlist." if no tracks are found.
    """
    # Query for the average duration of tracks in the given playlist
    avg_duration = db.query(func.avg(Track.duration_ms)).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        PlaylistTrack.pid == playlist_pid
    ).scalar()

    if avg_duration is None:
        return "No tracks found in the playlist."

    # Convert the average duration to seconds
    avg_duration_in_seconds = avg_duration / 1000

    return avg_duration_in_seconds


def get_playlist_artist_track_count(db: Session, playlist_pid: str):
    """
    Retrieves the count of tracks for each artist in the given playlist.

    Args:
        db (Session): The database session object.
        playlist_pid (str): The playlist PID.

    Returns:
        list: A list of dictionaries containing the artist name and the count of their tracks in the playlist.
    """
    # Query for each artist and the count of their tracks in the given playlist
    artist_track_count = db.query(
        Artist.artist_name,
        func.count(Track.track_uri).label('track_count')
    ).join(
        Track, Track.artist_uri == Artist.artist_uri
    ).join(
        PlaylistTrack, PlaylistTrack.track_uri == Track.track_uri
    ).filter(
        PlaylistTrack.pid == playlist_pid
    ).group_by(
        Artist.artist_name
    ).all()

    # Convert the result to a dictionary
    artist_track_count = [{"text": name, "value": count}
                          for name, count in artist_track_count]

    return artist_track_count

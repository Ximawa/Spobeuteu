from database import execute_query

def get_all_artists():
    query = "SELECT artist_uri FROM artists"
    result = execute_query(query)
    if result:
        return [row[0] for row in result]
    else:
        return []
    
def get_all_albums():
    query = "SELECT album_uri FROM albums"
    result = execute_query(query)
    if result:
        return [row[0] for row in result]
    else:
        return []
    
def get_all_tracks():
    query = "SELECT track_uri FROM tracks"
    result = execute_query(query)
    if result:
        return [row[0] for row in result]
    else:
        return []

def get_all_playlists():
    query = "SELECT pid FROM playlists"
    result = execute_query(query)
    if result:
        return [int(row[0]) for row in result]
    else:
        return []
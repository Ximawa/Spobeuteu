import mysql.connector
import time


DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'spobeuteu',
}

BATCH_SIZE_ARTISTS = 1000
BATCH_SIZE_ALBUMS = 5000
BATCH_SIZE_TRACKS = 7000
BATCH_SIZE_PLAYLISTS = 1000
BATCH_SIZE_PLAYLIST_TRACKS = 10000

conn = None


def get_connection():
    global conn
    if conn is None:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="spob"
        )
    return conn


def bulk_insert_artists(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data in batches
    batch_size = BATCH_SIZE_ARTISTS
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i+batch_size]
        cursor.executemany(
            "INSERT IGNORE INTO artists (artist_uri, artist_name) VALUES (%s, %s)", batch_values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_albums(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data in batches
    batch_size = BATCH_SIZE_ALBUMS
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i+batch_size]
        cursor.executemany(
            "INSERT IGNORE INTO albums (album_uri, album_name , artist_uri) VALUES (%s, %s, %s)", batch_values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_tracks(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data in batches
    batch_size = BATCH_SIZE_TRACKS
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i+batch_size]
        cursor.executemany(
            "INSERT IGNORE INTO tracks (track_uri, track_name, duration_ms, artist_uri, album_uri) VALUES (%s, %s, %s, %s, %s)", batch_values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_playlists(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data in batches
    batch_size = BATCH_SIZE_PLAYLISTS
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i+batch_size]
        cursor.executemany(
            "INSERT IGNORE INTO playlists (pid, name, num_albums, num_tracks, num_followers) VALUES (%s, %s, %s, %s, %s)", batch_values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_playlist_tracks(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data in batches
    batch_size = BATCH_SIZE_PLAYLIST_TRACKS
    for i in range(0, len(values), batch_size):
        batch_values = values[i:i+batch_size]
        cursor.executemany(
            "INSERT IGNORE INTO playlist_tracks (pid, track_uri, pos) VALUES (%s, %s, %s)", batch_values)

    # Commit the transaction
    cursor.execute("COMMIT")

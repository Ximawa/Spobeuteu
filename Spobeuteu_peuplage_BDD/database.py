import mysql.connector
import time


DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'spobeuteu',
}

conn = None


def get_connection():
    global conn
    if conn is None:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="spobeuteu"
        )
    return conn


def clear_tables():
    conn = get_connection()
    cursor = conn.cursor()

    tables = ['artists', 'albums', 'tracks', 'playlists', 'playlist_tracks']

    for table in tables:
        cursor.execute(f"DELETE FROM {table}")

    conn.commit()


def bulk_insert_artists(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data
    cursor.executemany(
        "INSERT IGNORE INTO artists (artist_uri, artist_name) VALUES (%s, %s)", values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_albums(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data
    cursor.executemany(
        "INSERT IGNORE INTO albums (album_uri, album_name, artist_uri) VALUES (%s, %s, %s)", values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_tracks(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data
    cursor.executemany(
        "INSERT IGNORE INTO tracks (track_uri, track_name, duration_ms, artist_uri, album_uri) VALUES (%s, %s, %s, %s, %s)", values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_playlists(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data
    cursor.executemany(
        "INSERT IGNORE INTO playlists (pid, name, num_followers,  num_tracks, num_albums) VALUES (%s, %s, %s, %s, %s)", values)

    # Commit the transaction
    cursor.execute("COMMIT")


def bulk_insert_playlist_tracks(values):
    conn = get_connection()
    cursor = conn.cursor()

    # Start a new transaction
    cursor.execute("START TRANSACTION")

    # Insert data
    cursor.executemany(
        "INSERT IGNORE INTO playlist_tracks (pid, track_uri, pos) VALUES (%s, %s, %s)", values)

    # Commit the transaction
    cursor.execute("COMMIT")

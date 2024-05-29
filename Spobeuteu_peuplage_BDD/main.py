import json
import os
from database import *

champsArtist = ["artist_uri", "artist_name"]
champsAlbum = ["album_uri", "album_name", "artist_uri"]
champsTrack = ["track_uri", "track_name",
               "duration_ms", "artist_uri", "album_uri"]
champsPlaylist = ["pid", "name", "num_followers", "num_tracks", "num_albums"]
champsPlaylistTrack = ["pid", "track_uri", "pos"]


def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    # clear_tables()

    data_dir = 'data'
    json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]

    # Seulement les 10 premiers fichiers pour test
    for json_file in json_files[:10]:
        file_path = os.path.join(data_dir, json_file)
        data = load_data(file_path)

        artistsValues = set()
        albumsValues = set()
        tracksValues = set()
        playlistsValues = set()
        playlistTracksValues = set()

        for playlist in data['playlists']:
            playlistValue = tuple(playlist.get(key, None)
                                  for key in champsPlaylist)
            playlistsValues.add(playlistValue)

            for track in playlist['tracks']:
                artistValue = tuple(track.get(key, None)
                                    for key in champsArtist)
                artistsValues.add(artistValue)

                albumValue = tuple(track.get(key, None) for key in champsAlbum)
                albumsValues.add(albumValue)

                trackValue = tuple(track.get(key, None) for key in champsTrack)
                tracksValues.add(trackValue)

                playlistTrackValue = (playlist.get(
                    'pid'), track['track_uri'], track.get('pos'))
                playlistTracksValues.add(playlistTrackValue)

        # Convert sets to lists before passing them to the bulk_insert functions
        bulk_insert_artists(list(artistsValues))
        bulk_insert_albums(list(albumsValues))
        bulk_insert_tracks(list(tracksValues))
        bulk_insert_playlists(list(playlistsValues))
        bulk_insert_playlist_tracks(list(playlistTracksValues))

    print("Données inserees avec succes")


if __name__ == "__main__":
    main()

import os

from spotify_client import SpotifyClient

#getting a random playlist of songs + add them to a library

def run():
    #Search spotipy for random songs
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track["id"] for track in random_tracks]
    # {id, name,....} only trying to get the track id

    #Once I get the list of random tracks, I'm adding them to my library
    was_added_to_library = spotify_client.add_track_to_library(track_ids)
    if was_added_to_library:
        for track in random tracks:
            print(f"Added {track["name"]} to your library")

if __name__ = "__main__"
run()
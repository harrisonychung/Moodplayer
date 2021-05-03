import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotify_client import SpotifyClient

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               #client_secret="YOUR_APP_CLIENT_SECRET",
                                               #redirect_uri="YOUR_APP_REDIRECT_URI",
                                               #scope="user-library-read"))"""

#getting a random playlist of songs + add them to a library

# 1) request auth URL
# 2) send user to auth url
# 3) user is redirected automatically to desired url (here, localhost:3000/something+token)
# 4) React app gathers token attached to that url, send to Flask so Flask can store it in session object
# 5) Flask can now gain access to spotify (and keep access using the refresh token logic) during our browsing session



util.prompt_for_user_token(
username='.yoharrison',
scope='user-library-read',
client_id='04eba6a8f0b64077965d175049476f60',  #04eba6a8f0b64077965d175049476f60
client_secret='3335d8fbaa90480983d54a164ecb89b8', #3335d8fbaa90480983d54a164ecb89b8
redirect_uri='http://localhost:5000') #http://localhost/

# # set open_browser=False to prevent Spotipy from attempting to open the default browser
# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False, 
# client_id='04eba6a8f0b64077965d175049476f60',
# client_secret='3335d8fbaa90480983d54a164ecb89b8',
# redirect_uri='http://localhost:5000'))

# print(spotify.me())


def run():
    #Search spotipy for random songs
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track["id"] for track in random_tracks]
    # {id, name,....} only trying to get the track id

    #Once I get the list of random tracks, I'm adding them to my library
    was_added_to_library = spotify_client.add_track_to_library(track_ids)
    if was_added_to_library:
        for track in random_tracks:
            #print(f"Added {track['name']} to your library")
            print("Added to Library")

if __name__ == "__main__":
    run()






    
import sys
import spotipy
import spotipy.util as util

import random

# - Steps:
#     - 1. Authenticating Spotipy
#     - 2. Creating a list of your favorite artists (get max 25) 
#         - API: Get a User’s Top Artists and Tracks
#         - Scope: user-top-read
#     - 3. For each of the artists, get all tracks for each artist. 
#         - API: Get an Artist’s Top Tracks
#     - 4. From top tracks, select tracks that are within a certain valence range 
#         - API: Get Audio Features for Several Tracks
#     - 5. From these tracks, create a playlist for user 
#         - API: Create a Playlist
#         - API: Add Tracks to a Playlist
#         - Scope: playlist-modify-public

client_id = ""
client_secret = ""
redirect_uri = ""

scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
	
	#Step 1. Authenticating Spotipy

	def authenticate_spotify():
		print('...connecting to Spotify')
		sp = spotipy.Spotify(auth=token)
		return sp

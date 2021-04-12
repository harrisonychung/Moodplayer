import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

#With user authentication 
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               #client_secret="YOUR_APP_CLIENT_SECRET",
                                               #redirect_uri="YOUR_APP_REDIRECT_URI",
                                               #scope="user-library-read"))"""

def authentication(token):
    print("Connecting to Spotify...")
    authorization = spotipy.Spotify(auth=token)
    return authorization

authentication(token):
print("Connecting to Spotify...")

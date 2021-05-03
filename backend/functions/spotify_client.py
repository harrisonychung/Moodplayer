import random
import requests
import string
import urllib
import sys
import spotipy
import spotipy.util as util

class SpotifyClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_tracks(self):
        #%q%
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        #generate a random character in string library / give alphabet characters in lowercase
        query = urllib.parse.quote(wildcard) 
        #pass in a URL to search spotify api
        offset = random.randint(0,1000) #spotify api offset max is 2000

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&track=track'

        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json", #expect back a JSON response
                "Authorization": f"User {self.api_key}"
            }
        )

        response_json = response.json()

        tracks = [track for track in response_json["tracks"]["items"]] #list comprehension 

        print(f"Found {len(tracks)} from your search")
        

        return tracks


    # def add_tracks_to_library(self, track_ids):
    #     url = "https://api.spotify.com/v1/me/tracks"

    #     response = requests.put(
    #         url,
    #         headers={
    #         "Content-Type": "application/json", #expect back a JSON response
    #             "Authorization": f"User {self.api_key}"
    #         },
    #         json={
    #             "ids": track_ids
    #         }
    #     )

    #     return response.ok



# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()

# scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
#     print(results)
# else:
#     print("Can't get token for", username)


#wildcards %%
#offset - which point onwards you want to get results


import random
import requests
import string
import urllib

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

        response = response.get(
            url,
            headers={
                "Content-Type": "application/json", #expect back a JSON response
                "Authorization": f"User {self.api_key}"
            }
        )

        response_json = response.json()

        tracks = [track for track in response_json["tracks"]["items"]]

        print(f"Found {len(tracks)} from your search")

        return tracks


    def add_tracks_to_library(self, track_ids):
        url = "https://api.spotify.com/v1/me/tracks"

        response = resquests.put(
            url,
            headers={
            "Content-Type": "application/json", #expect back a JSON response
                "Authorization": f"User {self.api_key}"
            },
            json={
                "ids": track_ids
            }
        )

        return response.ok

#wildcards %%
#offset - which point onwards you want to get results
from flask import Flask, flash, jsonify, redirect, render_template, request 
from requests.exceptions import HTTPError
import sqlite3
import sys
import spotipy 
import datetime
import time 
#from spotipy import util
import random

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard

CLI_ID = "04eba6a8f0b64077965d175049476f60"

CLI_SEC = "3335d8fbaa90480983d54a164ecb89b8"

REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read,user-follow-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True

class Spotify: 

    def __init__(self, auth):
        self.client = spotipy.Spotify(auth=auth)
    
    def get_token(token_info):
        token_valid = False
        print(token_info)
        #token_info = session.get("token_info", {})

        # Checking if the session already has a token stored
        if not token_info:
            token_valid = False
            return token_info, token_valid

        # Checking if token has expired
        now = int(time.time())
        later = int(token_info.get('expires_at'))
        difference = later - now
        print(now, later, difference)
        is_token_expired = difference < 60

        # Refreshing token if it has expired
        if (is_token_expired):
            # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
            sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
            token_info = sp_oauth.refresh_access_token(token_info.get('refresh_token'))
              

        token_valid = True
        return token_info, token_valid
      
    def authenticated_user_top_artists(self, limit=25): #creating list of favorite artists
        print('...getting your top artists')
        top_artists_name = []
        top_artists_uri = []

        time_ranges = ['short_term', 'medium_term', 'long_term']
        #short_term = 4 weeks, medium_term = 6 months long_term = complete history
        for r in time_ranges:
            top_artists_all_data = self.client.current_user_top_artists(limit=limit, time_range= r)
            top_artists_data = top_artists_all_data['items']
            for artist_data in top_artists_data:
                if artist_data["name"] not in top_artists_name:		
                    top_artists_name.append(artist_data['name'])
                    top_artists_uri.append(artist_data['uri'])

        followed_artists_all_data = self.client.current_user_followed_artists(limit=limit)
        followed_artists_data = (followed_artists_all_data['artists'])
        for artist_data in followed_artists_data["items"]:
            if artist_data["name"] not in top_artists_name:
                top_artists_name.append(artist_data['name'])
                top_artists_uri.append(artist_data['uri'])
        return top_artists_uri


    def authenticated_user_top_tracks(self, top_artists_uri):
        print("...getting top tracks")
        top_tracks_uri = [] 
        for artist in top_artists_uri:
            top_tracks_all_data = self.client.artist_top_tracks(artist)
            top_tracks_data = top_tracks_all_data['tracks']
            for track_data in top_tracks_data:
                top_tracks_uri.append(track_data['uri'])
        return top_tracks_uri
    

    def authenticated_user_mood_tracks(self, valence, energy, danceability, top_tracks_uri):

        print("...selecting your tracks")
        selected_tracks_uri = []
        random.shuffle(top_tracks_uri)
        print(len(top_tracks_uri))
        tracks_all_data = self.client.audio_features(top_tracks_uri[:100])

        current_index = 100
        tracks_all_data = []
        while (current_index - 100) < len(top_tracks_uri):
            tracks_all_data.extend(self.client.audio_features(top_tracks_uri[current_index - 100:current_index]))
            current_index += 100 

        for track_data in tracks_all_data:
            try:
                #print(track_data["valence"]

                if (valence - 0.25 <= track_data["valence"] <= (valence + 0.60)) and (energy - 0.25 <= track_data["energy"] <= (energy + 0.60)) and (danceability - 0.10 <= track_data["danceability"] <= (danceability + 0.80)):
                    selected_tracks_uri.append(track_data["uri"])                    
            except TypeError as te:
                continue
        return selected_tracks_uri
    
    # def authenticated_user_mood_tracks(self, valence, energy, danceability, top_tracks_uri):

    #     print("...selecting your tracks")
    #     selected_tracks_uri = []
    #     random.shuffle(top_tracks_uri)
    #     print(len(top_tracks_uri))
    #     tracks_all_data = self.client.audio_features(top_tracks_uri[:100])

    #     for track_data in tracks_all_data:
    #         distance = abs(track_data["valence"] - valence) + abs(track_data["danceability"] - danceability) + abs(track_data["energy"]) - energy)
    #         return distance / 3
    
    #     selected_tracks_uri.sort(authenticated_user_mood_tracks, descending=False)
    #     return selected_tracks_uri


      
    def authenticated_user_create_mood_playlist(self, selected_tracks_uri):
        print("...creating playlist")
        user_all_data=self.client.current_user()
        user_id = user_all_data["id"]
        current_time = datetime.datetime.now().strftime('%c')
        playlist_all_data = self.client.user_playlist_create(user_id, f"Moodplayer: {current_time}")
        playlist_id = playlist_all_data["id"]

        random.shuffle(selected_tracks_uri)
        print("LENGTH", len(selected_tracks_uri))
        try:
            self.client.user_playlist_add_tracks(user_id, playlist_id, selected_tracks_uri[0:35])
        except HTTPError:
            print("No tracks found")
        



# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, flash, jsonify, redirect, render_template, request 
import sqlite3
import sys
import spotipy
import time 
#from spotipy import util
import random

class Spotify: 

    def __init__(self, auth):
        self.client = spotipy.Spotify(auth=auth)
    
    def get_token(session):
        token_valid = False
        token_info = session.get("token_info", {})

        # Checking if the session already has a token stored
        if not (session.get('token_info', False)):
            token_valid = False
            return token_info, token_valid

        # Checking if token has expired
        now = int(time.time())
        is_token_expired = session.get('token_info').get('expires_at') - now < 60

        # Refreshing token if it has expired
        if (is_token_expired):
            # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
            sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
            token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

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
    

    def authenticated_user_mood_tracks(self, mood, top_tracks_uri):
        
        # if len(sys.argv) > 1:
        #     username = sys.argv[1]
        #     mood = float(sys.argv[2])
        # else:
        #     print("Usage: %s username" % (sys.argv[0],))
        #     sys.exit()

        print("...selecting your tracks")
        selected_tracks_uri = []
        random.shuffle(top_tracks_uri)
        print(len(top_tracks_uri))
        tracks_all_data = self.client.audio_features(top_tracks_uri[:100])
        for track_data in tracks_all_data:
            try:
                #print(track_data["valence"])
                if (mood - 0.10 <= track_data["valence"] <= (mood + 0.10)):
                    selected_tracks_uri.append(track_data["uri"])                    
            except TypeError as te:
                continue
        return selected_tracks_uri
      
    def authenticated_user_create_mood_playlist(self, selected_tracks_uri):
        print("...creating playlist")
        user_all_data=self.client.current_user()
        user_id = user_all_data["id"]
        playlist_all_data = self.client.user_playlist_create(user_id, "moodplayer")
        playlist_id = playlist_all_data["id"]

        random.shuffle(selected_tracks_uri)
        self.client.user_playlist_add_tracks(user_id, playlist_id, selected_tracks_uri[0:25])
    



# if __name__ == "__main__":
#     app.run(debug=True)

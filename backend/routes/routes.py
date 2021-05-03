from flask import Flask, render_template, redirect, request, session, jsonify, make_response,session,redirect
from flask_cors import CORS
import spotipy
from spotify import Spotify
#import spotipy.util as util
import time
import json 

app = Flask(__name__)
CORS(app)
app.secret_key = "SSK"

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard

CLI_ID = "04eba6a8f0b64077965d175049476f60"

CLI_SEC = "3335d8fbaa90480983d54a164ecb89b8"

REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read,user-follow-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True

# authorization-code-flow Step 1. Have your application request authorization; 
# the user logs in and authorizes access
@app.route("/start")
def verify():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)

@app.route("/api_callback")
def api_callback():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info.get("access_token")
    refresh_token = token_info.get("refresh_token")
    scope = token_info.get("scope")
    token_type = token_info.get("token_type")
    print(token_info)
    # Saving the access token along with all other token related info
    session["token_info"] = token_info
    return redirect(f"http://localhost:3000/login?access_token={access_token}&refresh_token={refresh_token}")
    

# Checks to see if token is valid and gets a new token if not
def get_token(session):
    print(session)
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

@app.route("/index", methods=["GET"])
def index():
    print(session)
    return render_template('landing.html')

@app.route("/topartist", methods=["GET"])
def get_top_artists():
    session['token_info'], authorized = Spotify.get_token(session)
    session.modified = True
    if not authorized:
        return jsonify(redirect('/'))
    harrison = Spotify(session.get("token_info").get("access_token"))
    return jsonify(harrison.authenticated_user_top_artists())

@app.route("/toptracks", methods=["GET"])
def get_top_tracks():
    session['token_info'], authorized = Spotify.get_token(session)
    session.modified = True
    if not authorized:
        return jsonify(redirect('/'))
    harrison = Spotify(session.get("token_info").get("access_token"))
    top_artists = harrison.authenticated_user_top_artists()  
    return jsonify(harrison.authenticated_user_top_tracks(top_artists))
    

@app.route("/moodtracks", methods=["GET"])
def get_user_mood_tracks():
    session['token_info'], authorized = Spotify.get_token(session)
    session.modified = True
    if not authorized:
        return jsonify(redirect('/'))
    harrison = Spotify(session.get("token_info").get("access_token"))
    top_artists = harrison.authenticated_user_top_artists() 
    top_tracks = harrison.authenticated_user_top_tracks(top_artists)
    return jsonify(harrison.authenticated_user_mood_tracks(.02,top_tracks))

@app.route("/moodplaylist", methods=["GET"])
def authenticated_user_create_mood_playlist():
    session['token_info'], authorized = Spotify.get_token(session)
    session.modified = True
    if not authorized:
        return jsonify(redirect('/'))
    harrison = Spotify(session.get("token_info").get("access_token"))
    top_artists = harrison.authenticated_user_top_artists()
    top_tracks = harrison.authenticated_user_top_tracks(top_artists)
    mood_tracks = harrison.authenticated_user_mood_tracks(.02, top_tracks)
    return jsonify(harrison.authenticated_user_create_mood_playlist(mood_tracks))

@app.route("/generateplaylist", methods=["POST"])
def moodplayer():
    token_info = response.get_json()
    session['token_info'], authorized = Spotify.get_token(token_info)
    print(session)
    session.modified = True
    if not authorized:
        return redirect('/')
    #data = request.get_json()
    #mood = data.get("mood")
    mood = request.form.get("mood")
    harrison = Spotify(session.get("token_info").get("access_token"))
    top_artists = harrison.authenticated_user_top_artists()
    top_tracks = harrison.authenticated_user_top_tracks(top_artists)
    mood_tracks = harrison.authenticated_user_mood_tracks(.02, top_tracks)
    harrison.authenticated_user_create_mood_playlist(mood_tracks)
    return jsonify({"success":True})
    
if __name__ == "__main__":
    app.run(debug=True)


# # @app.route("/topartist/<sp>", methods=["GET"])
# def get_top_artists(sp):
#     session['token_info'], authorized = get_token(session)
#     session.modified = True
#     if not authorized:
#         return jsonify(redirect('/'))
#     sp = spotipy.Spotify(auth=session.get("token_info").get("access_token"))
#     return jsonify(sp.current_user_top_artists(limit=10,))

	#data = request.get_json()
	#mood = data.get("mood")
	# token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
	#spotify_auth = get_token(session)
	#top_artists = authenticated_user_top_artists(spotify_auth) 
	#top_tracks = authenticated_user_top_tracks(spotify_auth, top_artists)
	#selected_tracks = authenticated_user_mood_tracks(spotify_auth, top_tracks, mood)
	#playlist = authenticated_user_create_mood_playlist(spotify_auth, selected_tracks, mood)
	#if not authorized:
		#return jsonify(redirect('/'))
	#harrison = Spotify(session.get("token_info").get("access_token"))
	#return jsonify(harrison.authenticated_user_create_mood_playlist())
from flask import Flask, render_template, redirect, request, session, jsonify, make_response,session,redirect
import spotipy
import spotipy.util as util
import time
import json 
app = Flask(__name__)

app.secret_key = "SSK"

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard

CLI_ID = "04eba6a8f0b64077965d175049476f60"

CLI_SEC = "3335d8fbaa90480983d54a164ecb89b8"

REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True


# authorization-code-flow Step 1. Have your application request authorization; 
# the user logs in and authorizes access
@app.route("/")
def verify():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)

@app.route("/index")
def index():
    return ("This Worked")

# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/api_callback")
def api_callback():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token along with all other token related info
    session["token_info"] = token_info


    return redirect("index")

# authorization-code-flow Step 3.
# Use the access token to access the Spotify Web API;
# Spotify returns requested data

# @app.route("/go", methods=['POST']) #GET 
# def go():
#     session['token_info'], authorized = get_token(session)
#     session.modified = True
#     if not authorized:
#         return redirect('/')
#     data = request.form
#     sp = spotipy.Spotify(auth=session.get().get())
#     response = sp.current_user_top_tracks(limit=data['num_tracks'], time_range=data['time_range']) 

@app.route("/go", methods=["GET"])
def go():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return jsonify(redirect('/'))
    sp = spotipy.Spotify(auth=session.get("token_info").get("access_token"))
    return jsonify(sp.current_user_top_tracks(limit=10,)) 



    # print(json.dumps(response))

    # return render_template("results.html", data=data)

# Checks to see if token is valid and gets a new token if not
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

if __name__ == "__main__":
    app.run(debug=True)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#gets 30 second samples + spotify image / cover art for the top 25 tracks for an artist

lz_uri = 'spotify:artist:0du5cEVh5yTK9QJze8zA0C?si=CP7YVAdLRUGM3xpbrGrcFw' #artist id // Bruno Mars

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials( client_id="04eba6a8f0b64077965d175049476f60" client_secret="3335d8fbaa90480983d54a164ecb89b8"))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:25]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()


for tracks in result    

for tracks in result 
import spotipy
import spotipy.util as util

#limit - the number of items to return (min = 1, default = 10, max = 50)
# Getting a set of tracks for each artist 

def set_tracks_for_artists(authentication, top_artists_uri):

    top_tracks_uri = []
    for artist in top_artists_uri:
        top_tracks_data = top_tracks_all_data['tracks']
		for track_data in top_tracks_data:
			top_tracks_uri.append(track_data['uri'])
	return top_tracks_uri


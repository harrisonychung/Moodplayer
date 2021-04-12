import spotipy
import spotipy.util as util



def mood_tracks_from_input(authentication, top_tracks_uri, mood):

    tracks_from_input_via_uri = []

    random.shuffle(top_tracks_uri)
    
    for tracks in list(group(top_tracks_uri, 25)):
        tracks_data = authentication.audio_features(tracks)
        for track_data in tracks_all_data
    try:
        
        if mood < 0.10:
            track_data["valence"]
        

    
    except TypeError 
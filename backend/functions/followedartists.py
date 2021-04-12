import spotipy
import spotipy.util as util

#Creating a list of top followed artists.
#limit - the number of items to return (min = 1, default = 10, max = 50)
#Function for creating a list of a user's favorite artists from artists they are already following

def followed_artists(authorization):
    users_top_artists_name = []
    users_top_artists_uri = []

    time_ranges = ["short_term", "medium_term", "long_term"] 
    #short_term = 4 weeks medium_term = 6 months long_term = complete history

    
    for r in time_ranges:
       followed_artists_alldata = authorization.current_user_followed_artists(limit=25 time_range="long_term") #data for all time
       followed_artists_data = followed_artists_alldata["artists"]
       for artist_data in followed_artists_data["items"]:
           if artist_data["name"] not in user_top_artists_name:
               users_top_artists_name.append(artist_data["name"])
               users_top_artists_uri.append(artist_data["uri"])
    
    return users_top_artists_uri


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import util
import sys

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""
SCOPE = "user-library-read playlist-modify-public"
playlist_id = sys.argv[1]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))
playlist_keys = util.get_playlist_key(sp, playlist_id)
new_order = util.order_by_key(playlist_keys)
util.generate_new_playlist(sp, new_order, playlist_id)









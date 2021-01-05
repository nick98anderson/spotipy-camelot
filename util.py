import random

def order_by_key(track_dict):

    order = []
    step = random.choice(list(track_dict.keys()))
    key = track_dict[step][0]
    mode = track_dict[step][1]
    order.append(step)
    valid_keys = camelot(key,mode)
    valid_step = False

    while len(order) < len(track_dict.keys()):
        for ckey, cvalue in track_dict.items():
            if ckey not in order and cvalue in valid_keys:
                valid_step = True
                step = ckey
                order.append(step)
                valid_keys = camelot(cvalue[0], cvalue[1])
            else:
                valid_step = False
        if valid_step == False:
            step = random.choice(list(track_dict.keys()))
            while step in order:
                step = random.choice(list(track_dict.keys()))
            order.append(step)
        
    return order


def get_playlist_key(spotify,playlist_id):
    track_keys = {}
    tracks = spotify.playlist_items(playlist_id=playlist_id)
    for track in tracks['items']:
        track_id = track['track']['id']
        audio_features = spotify.audio_features(track_id)[0]
        track_key = audio_features['key']
        track_mode = audio_features['mode']
        track_keys[track_id] = [track_key, track_mode]

    return track_keys


def generate_new_playlist(sp, playlist_orderd,old_playlist_id):
    user_id = sp.me()['id']
    old_name = sp.user_playlist(user=user_id, playlist_id=old_playlist_id)['name']
    new_name = old_name + " reorderd"
    playlist_id = sp.user_playlist_create(user=user_id, name=new_name)['id']
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=playlist_orderd)


def camelot(key, mode):
    valid_keys = []

    if key == 11:
        valid_keys.append([10,mode])
        valid_keys.append([0,mode])
        valid_keys.append([key,mode])
        if mode == 1:
            valid_keys.append([key, 0])
        else:
            valid_keys.append([key,mode])

    elif key == 0:
        valid_keys.append([1, mode])
        valid_keys.append([11, mode])
        if mode == 1:
            valid_keys.append([key, 0])
        else:
            valid_keys.append([key,mode])
    else:
        valid_keys.append([key+1, mode])
        valid_keys.append([key-1, mode])
        valid_keys.append([key,mode])
        if mode == 1:
            valid_keys.append([key, 0])
        else:
            valid_keys.append([key, 1])

    return valid_keys

def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    MAX_SPEED = 1.25

    if speed < MAX_SPEED:
        reward = 0.4
    else:
        reward = 0.8

    marker_1 = 0.165 * track_width
    marker_2 = 0.33 * track_width
    marker_3 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward = reward + 1.0
    elif distance_from_center <= marker_2:
        reward = reward + 0.7
    elif distance_from_center <= marker_3:
        reward = reward + 0.3
    else:
        reward = 1e-3

    if not all_wheels_on_track:
        reward = 1e-3

    return float(reward)

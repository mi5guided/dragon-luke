def reward_function(params):
    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = 9000
    else:
        reward = 0.01
    return float(reward)

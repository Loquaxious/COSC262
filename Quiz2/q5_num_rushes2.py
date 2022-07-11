def num_rushes(slope_height, rush_height_gain, back_sliding, climbed=0):
    """Calculates how many dashes Herbet need to do to get up scree slope """
    
    if rush_height_gain >= slope_height:
        return 1
    else:
        climbed += rush_height_gain
        if climbed >= slope_height:
            return 1
        else:
            return 1 + num_rushes(slope_height, rush_height_gain * 0.95, \
                                  back_sliding * 0.95, climbed - back_sliding)
        
ans = num_rushes(100, 15, 7)
print(ans)        
ans = num_rushes(10, 10, 9)
print(ans)        

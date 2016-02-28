import numpy as np

def naming_seasons(seasons_arr):
    """Creates a list of named seasons
    
    Parameters
    ----------
        seasons_arr: array of numeric strings
        
    Returns:
    --------
        new_seasons: array of named seasons
    """
    new_seasons = []
    for s in seasons_arr:
        if s == 1:
            new_seasons.append('Fall')
        elif s == 2:
            new_seasons.append('Winter')
        elif s == 3:
            new_seasons.append('Spring')
        else:
            new_seasons.append('Summer')
    
    return np.array(new_seasons)

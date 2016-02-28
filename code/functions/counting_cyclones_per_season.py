import numpy as np

def counting_cyclones_per_season(seasons_str, counts_arr):
    """Counts number of cyclones per season
    
    Parameteres
    -----------
        seasons_str: str array with named seasons
        counts_arr: int array with cyclone counts
    
    Returns
    -------
        total_cyclones: dictionary with seasons as keys, and totals as values
    """
    total = np.zeros(4, np.int)
    aux = list(set(seasons_str))
    for i in range(total.size):
        total[i] = sum(counts_arr[seasons_str == aux[i]])
    total_cyclones = dict(zip(aux, total))
    return total_cyclones

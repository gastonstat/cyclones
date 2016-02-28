
def counting_cyclones_per_season(season, count):
    """Counts total number of cyclones per season
    
    Parameteres
    -----------
        season: list with str-numeric seasons
        - 1: Fall
        - 2: Winter
        - 3: Spring
        - 4: Summer
        count: list with number of cyclones
    
    Returns
    -------
        totals: list with total number of cyclones per season
    """
    totals = [0, 0, 0, 0]
    for num in range(0, len(season)):
        if season[num] == '1':
            totals[0] = totals[0] + count[num]
        elif season[num] == '2':
            totals[1] = totals[1] + count[num]
        elif season[num] == '3':
            totals[2] = totals[2] + count[num]
        else:
            totals[3] = totals[3] + count[num]
    # output
    return totals



def get_total_cyclones(file_name):
    """Read data and return list of cyclones
    
    Parameteres
    -----------
        file_name: name of file
    
    Returns
    -------
        totals: list with total number of cyclones per season
    """
	myfile = open(file_name)
	content = myfile.readlines()
	seasons = []
	counts = []
	for line in content:
		aux = line.strip()
		values = aux.split()
		seasons.append(values[1])
		counts.append(int(values[2]))

	myfile.close()
	# get total cyclones
	totals = total_cyclones(seasons, counts)
	# output
	return(totals)

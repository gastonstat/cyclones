
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
import numpy as np
import matplotlib.pyplot as plt
from naming_seasons import *
from counting_cyclones_per_season import *
from make_cyclones_table import *


data_directory = "../../data/"

# Load cyclone.dat
data_file = data_directory + 'cyclone.dat'
data = np.loadtxt(data_file, dtype = 'int')

# extract seasons and counts
seasons = data[:,1]
counts = data[:,2]

named_seasons = naming_seasons(seasons)

total_cyclones = counting_cyclones_per_season(named_seasons, counts)

# barchart
index = np.arange(len(total_cyclones.keys()))
heights = total_cyclones.values()
bar_width = 0.35
opacity = 0.4
# bar chart
sys.stdout.write("Creating bar chart\n")
plt.bar(index, heights, bar_width, alpha=opacity, color='b')
plt.xlabel('Season')
plt.ylabel('Cyclones')
plt.title('Total cyclones per season')
plt.xticks(index + bar_width, total_cyclones.keys())
plt.savefig('../../images/barchart_cyclones.png')
plt.close()


# create latex table
sys.stdout.write("Creating latex table\n")
latex_table = make_cyclones_table(total_cyclones)

# write table to a .tex file
sys.stdout.write("Exporting latex table\n")
tex_file = open('../../report/sections/cyclones_table.tex', 'w')
for elem in latex_table:
    tex_file.write(elem)
tex_file.close()

sys.stdout.write("Finished writing cyclones_table.tex\n")

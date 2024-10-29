import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = 0
## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, skiprows= 2, delimiter= ',')
elapsedTime = data[:,0]
MLII = data[:,1]
V1 = data[:,2]
plt.title('Signal for ' + database_name)
plt.plot(data)
plt.show()
"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""


## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""
difference = np.diff(V1)
plt.title('Difference Signal for ' + database_name)
plt.plot(difference)
plt.show()
## YOUR CODE HERE ##


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##

sq = np.square(difference)
plt.title('Squared Signal for ' + database_name)
plt.plot(sq)
plt.show()
"""
Step 5: Pass a moving filter over your data
"""
compare = np.ones(7)
signal = np.convolve(sq, compare)
## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Filtered Signal for ' + database_name)
plt.plot(signal)
plt.show()
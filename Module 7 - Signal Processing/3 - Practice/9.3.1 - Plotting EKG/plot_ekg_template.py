
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
Data = np.loadtxt(path, skiprows= 2, delimiter= ',')
### Your code here ###

# save each vector as own variable
elapsedTime = Data[:,0]
MLII = Data[:,1]
V1 = Data[:,2]
### Your code here ###

# use matplot lib to generate a single
plt.plot(elapsedTime, V1)
plt.plot(elapsedTime, MLII)
plt.show()
### Your code here ###
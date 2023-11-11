import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#initalize csv file name
csvname = 'Dry_Bean_Dataset.csv'
#load the csv file
data = np.loadtxt(csvname,delimiter = ',')
# feature values
xData = data[:-1,:]
yData = data[-1:,:]
# Convert them to numpy arrays
x = np.array(xData)
y = np.array(yData)
# adding Bias to the points
x = np.row_stack([np.ones(x.shape[1]), x])
print(x, y)
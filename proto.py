import matplotlib
import scikit 

#initalize csv file name
csvname = 'credit_dataset.csv'
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
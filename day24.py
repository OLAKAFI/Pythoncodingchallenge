# STATISTICS
import numpy as np

# Creating numpy array using
python_list = [1,2,3,4,5]
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

numpy_array_from_list = np.array(python_list, dtype=float)
print(type(numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list)         # array([1, 2, 3, 4, 5])


# Creating a boolean array
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])
print(type(numpy_bool_array))

# Creating numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

# Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)

# Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

print('---------------------------------------------------------------------------------------------------')
# Mathematical Operations with numpy
list = [1,2,3,4,5,6]
numpy_list = np.array(list)
print('Add 10 to array list: ', 5 + numpy_list)

print('---------------------------------------------------------------------------------------------------')
# Getting items from a numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print('Shape of array is {} while the size of the array is {} '.format(two_dimension_array.shape, two_dimension_array.size))

# Getting rows from multi dimentional arrays
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
first_col = two_dimension_array[:,0]
second_col = two_dimension_array[:,1]
third_col = two_dimension_array[:,2]
print('first row: {}, second row: {} and third row: {}'.format(first_row,second_row,third_row))
print('first col: {}, second col: {} and third col: {}'.format(first_col,second_col,third_col))


print('---------------------------------------------------------------------------------------------------')
# Slicing Numpy Array
three_dimension_array = np.array([[1,2,5,3],[4,5,5,6], [7,8,3,9]])
first_three_rows_and_columns = three_dimension_array[0:2, 0:2]    # two_dimension_array[col, row]
print(first_three_rows_and_columns)

print('---------------------------------------------------------------------------------------------------')
# Reversing an rows in an array
print('Reversed Rows: ', three_dimension_array[::,::-1])

# Reversing columns in an array
print('Reversed Column: ', three_dimension_array[::-1,::])

print('---------------------------------------------------------------------------------------------------')
# Stacking Lists
# Horitzontal Stack    
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))


print('---------------------------------------------------------------------------------------------------')
# Generating Random Numbers
# Generate random float numbers
rand_float = np.random.random(5)
print('Five Random float numbers: ', rand_float)
# Generate random integer numbers
rand_int = np.random.randint(3,8, size=5)
print('Five random integers between 3 and 8:', rand_int)

print('-----------------------------------------------------------------------------------------------------')
# NUMPY AND STATISTICS
import matplotlib.pyplot as plt
import seaborn as sns

# Arrange in Numpy like range in normal python
even = np.arange(0,15,2)
print('Even numbers between 0 and 15: ', even)


print('-----------------------------------------------------------------------------------------------------')
# Rows and Cols with minimum and maximum
print(two_dimension_array)
two_dimension_array[0,1] = 0
print(two_dimension_array)
print('Minimum in Coumns: ', np.amin(two_dimension_array, axis=0))
print('Maximum in Colums: ', np.amax(two_dimension_array, axis=0))
print('Manimum in rows: ', np.amin(two_dimension_array, axis=1))
print('Maximum in rows: ', np.amax(two_dimension_array, axis=1))


print('-----------------------------------------------------------------------------------------------------')
# Statistical Functions with Numpy
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 200)
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ',np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()


# Generating relationship through plots
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
plt.plot(temp, pressure)
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title('Temperature vs Pressure Chart')
plt.xticks(np.arange(0,6,0.5))
plt.show()


#Guassian Plot
mu = 28 # mu is mean
sigma = 15  # sigma is standard deviation
samples = 100000   
x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()


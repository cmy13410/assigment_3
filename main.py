import numpy as np
from numpy import linalg as lng
import matplotlib.pyplot as mpl


# Question 1

# Question 1.a
base_array = np.random.randint(1, 21, size=15)  # creates base_array for future use

# print results
print("Question 1.a:")
print("Generated array: \n", base_array)

reshaped_array = np.reshape(base_array, (3, 5))  # creates reshaped_array
print("Reshaped array: \n", reshaped_array)  # print results

# replace the max in each row by zero
replace_array = np.amax(reshaped_array, axis=1)  # Creates array of the max value of each row
count = 0  # Sets count to 0 so that the replace_array can be iterated through separately
num_rows, num_cols = reshaped_array.shape  # Saves number of columns and rows
for i in range(num_rows):  # Loops through and updates by row
    for j in range(num_cols):
        if reshaped_array[i, j] == replace_array[count]:  # If the value at the idx = the max value of the row
            reshaped_array[i, j] = 0  # Replaces max value with 0
    count += 1  # increments count to iterate through replace_array
# print results
print("Replace the max value in each row with 0:\n", reshaped_array)

# create 2-D 4x3 array and print shape, type, datatype,
array = np.arange(1, 13)  # creates base_array for future use
print("Print shape, type, and datatype: ")
print("Shape: ", array.shape)
print("Type: ", type(array))
print("Datatype: ", array.dtype)


# Question 1.b
print("\nQuestion 1.b:")
eigenvalues, eigenvectors = lng.eig(np.array([[3, -2], [1, 0]]))  # Uses numpy libaray function, eig
print("eigenvalues: \n", eigenvalues)
print("eigenvectors: \n", eigenvectors)

# Question 1.c
print("\nQuestion 1.c")
traced_array = np.trace([[0, 1, 2],[3, 4, 5]]) # Uses numpy libaray function, trace
print("Traced array: \n", traced_array)

# Question 1.d
print("\nQuestion 1.d")
updated_array_1 = np.reshape([[1, 2], [3, 4], [5, 6]], (3, 2))  # creates reshaped_array
print("Reshaped array:\n", updated_array_1)

updated_array_2 = np.reshape([[1, 2, 3], [4, 5, 6]], (2, 3))  # creates reshaped_array
print("Reshaped array:\n", updated_array_2)

# Question 2
labels = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

explode = (0.1, 0, 0, 0, 0, 0)  # explode biggest slice
mpl.pie(popularity, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=130) # Uses arguments to create desired chart
mpl.show()


# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import csv

# define list of period numbers for which we have data
period_numbers = [2,4,6,8,10,15,20,25,30,35,40,45]

# create a list of file names
file_names = []
for i in period_numbers:
    file_names.append('period_' + str(i) + '.csv')

# for each file name, open it and read the first column into a list of measured times
measured_times = []

for file_name in file_names:
    # open the csv file
    with open(r"C:\Users\maxst\sciencia\F23\PHYS397\Labs\2\\"+file_name, 'r') as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file)
        # create a list of the first column of the csv file
        times = []
        for row in csv_reader:
            # skip the first row as it is a header
            if row[0] == 'Time (s)':
                continue
            times.append(float(row[0]))
        # append the list of times to the list of measured times
        measured_times.append(times)


print(measured_times)



# we need to alter each element of measured times - the first element in each list times is the time at which the pendulum was released
# we need to subtract each time from the time following it to  'normalize' it

for i in range(len(measured_times)):
    for j in range(len(measured_times[i])):
        measured_times[i][j] = measured_times[i][j] - measured_times[i-1][j]


print(measured_times)


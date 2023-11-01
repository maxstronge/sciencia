# import necessary packages to transpose a list of csv files
import csv


period_numbers = [2,4,6,8,10,15,20,25,30,35,40,45]

# create a list of file names
file_names = []
for i in period_numbers:
    file_names.append('period_' + str(i) + '.csv')


    

# transpose all the csv files in file_names

for file_name in file_names:
    # open the csv file
    with open(r"C:\Users\maxst\sciencia\F23\PHYS397\Labs\2\\"+file_name, 'r') as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file)
        # transpose the csv file
        transposed = zip(*csv_reader)
        # write the transposed csv file
        with open('transposed_' + file_name, 'w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file)
            csv_writer.writerows(transposed)

        
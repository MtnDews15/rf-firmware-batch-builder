from helper import *
from pandas import *

csvfile = pandas.read_csv('5522.csv')

coordinates = []
for index, row in csvfile.iterrows():
    coordinates.append((row["Latitude"], row["Longitude"]))

boolean_matrix = rough_matrix(coordinates) > 13

group_matrix = [[] for i in range(len(boolean_matrix))]
for row_i, row in enumerate(boolean_matrix):
    group_matrix[row_i] = list([i for i, is_true in enumerate(row) if is_true])

group_dictionary = dict()
for i, values in enumerate(group_matrix):
    group_dictionary[i] = values

print(start(group_dictionary))

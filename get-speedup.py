import argparse
import numpy
import re

parser = argparse.ArgumentParser(description='Compute speed up values for a given data file in CSV format.')
parser.add_argument('data_path', metavar='DATA_FILE', help='this file contains benchmark data in CSV format')
parser.add_argument('output_path', metavar='RESULT_FILE', help='the results will be stored in this file')

args = parser.parse_args()
data_path = args.data_path
output_path = args.output_path

###############################################################################
# IMPORT DATA
###############################################################################

input_data = numpy.genfromtxt(data_path, delimiter=';')
# print 'input data:', input_data

###############################################################################
# COMPUTE SPEED-UP
###############################################################################

values = []
baseline = input_data[0][1]
for row in input_data:
    num_threads = row[0]
    value = row[1]
    values.append((int(num_threads), value / baseline))

###############################################################################
# EXPORT
###############################################################################

result_file = open(output_path, 'w')
for (num_threads, value) in values:
    line = str(num_threads) + ';' + str(value)
    result_file.write(line + '\n')

result_file.close()

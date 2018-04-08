import argparse
import numpy

parser = argparse.ArgumentParser(description='Compute parallel efficiency values for a given data file in CSV format.')
parser.add_argument('data_path', metavar='DATA_FILE', help='this file contains speedup data in CSV format')
parser.add_argument('output_path', metavar='RESULT_FILE', help='the results will be stored in this file')

args = parser.parse_args()
data_path = args.data_path
output_path = args.output_path

###############################################################################
# IMPORT DATA
###############################################################################

header = numpy.genfromtxt(data_path, delimiter=';', dtype=None, encoding=None, max_rows=2)
store_name = header[0][1]
sc_name = header[1][1]

input_data = numpy.genfromtxt(data_path, delimiter=';', skip_header=2)

###############################################################################
# COMPUTE SPEED-UP
###############################################################################

values = []
baseline = input_data[0][1]
for row in input_data:
    num_threads = row[0]
    speedup = row[1]
    # print speedup, '/', num_threads
    values.append((int(num_threads), speedup / num_threads))

###############################################################################
# EXPORT
###############################################################################

result_file = open(output_path, 'w')

# write header
result_file.write('store;' + store_name + '\n')
result_file.write('sc;' + sc_name + '\n')

# write values
for (num_threads, value) in values:
    line = str(num_threads) + ';' + str(value)
    result_file.write(line + '\n')

result_file.close()

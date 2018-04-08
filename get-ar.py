import argparse
import numpy
import sys

parser = argparse.ArgumentParser(description='Compute abort rates for a given data file in CSV format.')
parser.add_argument('data_path', metavar='DATA_FILE', help='this file contains abort count data in CSV format')
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

num_txs = 1000

values = []
baseline = input_data[0][1]
for row in input_data:
    num_threads = row[0]
    num_aborts = row[1]
    abort_rate = 100 * num_aborts / num_txs
    # print num_aborts, '/', num_txs, '=>', abort_rate
    values.append((int(num_threads), abort_rate))

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

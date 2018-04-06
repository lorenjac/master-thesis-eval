from os import walk
import argparse
import re

parser = argparse.ArgumentParser(description='Compute average values for a given parameter for all .log files in a given folder.')
parser.add_argument('log_dir', metavar='LOG_DIR', help='path to a folder with .log files')
parser.add_argument('param', metavar='PARAM', help='the parameter to be processed (e.g. throughput)')
parser.add_argument('output_path', metavar='RESULT_FILE', help='the results will be stored in this file')

args = parser.parse_args()
log_dir = args.log_dir
param = args.param
output_path = args.output_path

###############################################################################
# GET LIST OF LOG FILES
###############################################################################

matches = re.findall('.*-(\w*)-(\w*)', log_dir)
if not matches or len(matches[0]) != 2:
    raise Exception('invalid path (expected format is date-store-scenario)')

store_name = matches[0][0]
sc_name = matches[0][1]

f = []
for (dirpath, dirnames, filenames) in walk(log_dir):
    f.extend(filenames)
    break

f = filter(lambda e: e.endswith('.log'), f)

###############################################################################
# AGGREGATION OF PARAMETER VALUES FROM DIFFERENT FILES
###############################################################################

dataset = []
for fileName in f:
    # parse number of cores used for benchmark
    num_threads_parse = re.findall('(\d+)', fileName)
    if num_threads_parse:
        num_threads = int(num_threads_parse[0])
        # print 'num_threads =', num_threads

    # read file
    file = open(log_dir + '/' + fileName, 'r')
    lines = file.readlines()
    file.close()

    # find and parse parameter value of interest
    values = []
    for line in lines:
        value = re.findall(param + '=(\d*\.\d+|\d+).*', line)
        if value:
            values.append(float(value[0]))

    if not values:
        print 'warning: no values for parameter + <' + param + '>'
        continue

    avg = sum(values) / len(values)
    dataset.append((num_threads, avg))

###############################################################################
# POST-PROCESSING
###############################################################################

dataset = sorted(dataset, key=lambda pair: pair[0])

###############################################################################
# EXPORT
###############################################################################

result_file = open(output_path, 'w')

# write header
result_file.write('store;' + store_name + '\n')
result_file.write('sc;' + sc_name + '\n')

# write values
for (num_threads, result) in dataset:
    result_file.write(str(num_threads) + ';' + str(result) + '\n')

result_file.close()

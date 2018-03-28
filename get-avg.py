from os import walk
import sys
import re

# path = 'log'
path = sys.argv[1]
# parameter = 'throughput'
parameter = sys.argv[2]

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

f = filter(lambda e: e.endswith('.log'), f)

#######################################################################
# AVERAGE
#######################################################################

dataset = []
for fileName in f:
    print fileName

    # parse number of cores used for benchmark
    num_threads_parse = re.findall('(\d+)', fileName)
    if num_threads_parse:
        num_threads = int(num_threads_parse[0])
        print 'num_threads =', num_threads

    # read file
    file = open(path + '/' + fileName, 'r')
    lines = file.readlines()
    file.close()

    # find and parse parameter value of interest
    values = []
    for line in lines:
        value = re.findall(parameter + '=(\d*\.\d+|\d+).*', line)
        if value:
            # print parameter, '=', value
            # values.extend(value)
            values.append(float(value[0]))
    print 'values =', values

    avg = sum(values) / len(values)
    dataset.append((num_threads, avg))

dataset = sorted(dataset, key=lambda pair: pair[0])
print dataset

paramAvgFile = open(path + '/' + parameter + '_avg.csv', 'w')

# write header
header = '' + str(dataset[0][0]) + 'T'
for (num_threads, result) in dataset[1:]:
    header += ';' + str(num_threads) + 'T'
paramAvgFile.write(header)
paramAvgFile.write('\n')

# write values
values = '' + str(dataset[0][1])
for (num_threads, result) in dataset[1:]:
    values += ';' + str(result)
paramAvgFile.write(values)

paramAvgFile.close()

#######################################################################
# IMPROVEMENT
#######################################################################

# compute improvements between thread counts
impr = []
base = dataset[0][1]
for (num_threads, result) in dataset[1:]:
    impr.append((num_threads, result / base))
    # base = result

print impr

# create file to store improvements
imprFile = open(path + '/' + parameter + '_imp.csv', 'w')

# write header
imprHeader = '' + str(impr[0][0]) + 'T'
for (num_threads, result) in impr[1:]:
    imprHeader += ';' + str(num_threads) + 'T'
imprFile.write(imprHeader)
imprFile.write('\n')

# write values
imprValues = '' + str(impr[0][1])
for (num_threads, result) in impr[1:]:
    imprValues += ';' + str(result)
imprFile.write(imprValues)

imprFile.close()

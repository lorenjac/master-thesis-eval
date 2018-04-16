import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import numpy

parser = argparse.ArgumentParser(description='Plot benchmark results.')
parser.add_argument('files', metavar='FILES', type=str, nargs='+')
parser.add_argument('-o', '--output', metavar='FILE', help='the results will be stored in this file')

args = parser.parse_args()
output_path = args.output
sample_paths = args.files

###############################################################################
# IMPORT DATA
###############################################################################

samples = []
for path in sample_paths:
    header = numpy.genfromtxt(path, delimiter=';', dtype=None, encoding=None, max_rows=2)
    store_name = header[0][1]
    sc_name = header[1][1]
    data = numpy.transpose(numpy.genfromtxt(path, delimiter=';', skip_header=2))
    samples.append((store_name, sc_name, data))

###############################################################################
# PLOT DATA
###############################################################################

plt.style.use('ggplot')

###############################################################################
# AXES
###############################################################################

# x = [1, 2, 4, 8, 16, 32]
sample_pts = samples[0][2][0]
x = map (lambda e: int(e), sample_pts)

#### x-axis
# plt.xticks()
# plt.xticks([1,2,4,8,12,16,20,24,28,32])
# plt.xscale('log', basex=2)
plt.xlabel('Number of Threads')

#### y-axis
plt.ylabel('Transactions per second')
# plt.yscale('log')

# leave some space
# plt.axis([x[0]-1, x[len(x)-1]+1, midas_data[0]-1, midas_data[len(midas_data)-1]+1])

###############################################################################
# GRAPHS
###############################################################################
#
#   color:
#       b    g     r   c    m       y      k     w
#       blue green red cyan magenta yellow black white
#
#   segments:
#       -     --      -.      :       .
#
#   dots
#       o     x       +

# perfect_line, = plt.plot(x, x, 'k--', label='Ideal')

# lines = [perfect_line]
lines = []
color_idx = 0
colors = ['b',  'r',  'g',  'c',  'm',  'y']
for (store, sc, values) in samples:
    capitalized_name = store[0].upper() + store[1:]
    if capitalized_name == 'Midas optimized':
        capitalized_name = 'Midas*'
    # line, = plt.plot(x, values[1], colors[color_idx] + 'o-', label=capitalized_name + ' (' + sc + ')')
    line, = plt.plot(x, values[1], colors[color_idx] + 'o-', label=capitalized_name)
    # line, = plt.plot(x, map(lambda e: e/1000.0, values[1]), colors[color_idx] + 'o-', label=capitalized_name)
    color_idx = (color_idx + 1) % len(colors)
    lines.append(line)

###############################################################################
# LEGEND
###############################################################################

plt.legend(handles=lines, loc='best')
# plt.legend(handles=lines, loc='upper right')
# plt.legend(handles=lines)

###############################################################################
# EXPORT
###############################################################################

if output_path:
    plt.savefig(output_path)
else:
    plt.show()

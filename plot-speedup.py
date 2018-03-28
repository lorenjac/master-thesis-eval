import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import numpy
import sys

midas_data_file=sys.argv[1]
echo_data_file=sys.argv[2]
output_file=sys.argv[3]

print 'midas data loc:', midas_data_file
print 'echo data loc:', echo_data_file

###############################################################################
# IMPORT DATA
###############################################################################

midas_data = numpy.genfromtxt(midas_data_file, delimiter=';', skip_header=1)
print 'midas data:', midas_data

echo_data = numpy.genfromtxt(echo_data_file, delimiter=';', skip_header=1)
print 'echo data:', echo_data

###############################################################################
# PLOT DATA
###############################################################################

plt.style.use('ggplot')

###############################################################################
# AXES
###############################################################################

x = [2, 4, 8, 16, 32]

#### x-axis
# plt.xticks()
# plt.xticks([1,2,4,8,12,16,20,24,28,32])
# plt.xscale('log', basex=2)
plt.xlabel('threads')

#### y-axis
plt.ylabel('speedup')
# plt.yscale('log')

# leave some space
# plt.axis([x[0]-1, x[len(x)-1]+1, midas_data[0]-1, midas_data[len(midas_data)-1]+1])

###############################################################################
# GRAPHS
###############################################################################
#
#   color:
#     b   blue
#     g   green
#     r   red
#     c   cyan
#     m   magenta
#     y   yellow
#     k   black
#     w   white
#   line segments:
#     -
#     --
#     -.
#     :
#     .
#   dots
#     o
#     x
#     +
perfect_line, = plt.plot(x, x, 'k--', label='Ideal')
midas_line, = plt.plot(x, midas_data, 'bo-', label='Midas')
echo_line, = plt.plot(x, echo_data, 'ro-', label='Echo')

###############################################################################
# LEGEND
###############################################################################

# plt.legend(handles=[midas_line, echo_line])
plt.legend(handles=[midas_line, echo_line, perfect_line])

# plt.legend(handles=[midas_line, echo_line], loc='best')
plt.legend(handles=[midas_line, echo_line, perfect_line], loc='best')

# plt.legend(handles=[midas_line, echo_line], loc='lower right')
plt.legend(handles=[midas_line, echo_line, perfect_line], loc='upper right')

###############################################################################
# EXPORT
###############################################################################

plt.savefig(output_file)
plt.show()

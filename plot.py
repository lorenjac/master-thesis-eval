import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

plt.style.use('ggplot')

# tx throughput
# x = [1, 2, 4, 8, 16, 32]
# midas_txt = [3200, 6000, 11000, 18000, 22000, 24000]
# echo_txt = [500, 1000, 1500, 2000, 2500, 3000]

# speed up
x = [2, 4, 8, 16, 32]
midas_txt = [1.875 , 1.833 , 1.633 , 1.222 , 1.099]
echo_txt =  [2.0   , 1.5   , 1.333 , 1.25  , 1.2]

# x-axis ticks and scaling
plt.xticks(x)
# plt.xticks([1,2,4,8,12,16,20,24,28,32])
# plt.xscale('log', basex=2)

# x-axis ticks and scaling (tx throughput)
# plt.yticks([250, 500, 1000, 2000, 5000, 10000, 15000, 20000, 25000])
# plt.yscale('log')

# x-axis ticks and scaling (speed up)
# plt.yscale('log')

# leave some space
# plt.axis([x[0]-1, x[len(x)-1]+1, midas_txt[0]-1, midas_txt[len(midas_txt)-1]+1])

# lines
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
midas_line, = plt.plot(x, midas_txt, 'bo-', label='Midas')
echo_line, = plt.plot(x, echo_txt, 'ro-', label='Echo')

# axis labels
plt.xlabel('threads')
plt.ylabel('transactions per second')

# legend
plt.legend(handles=[midas_line, echo_line])
plt.legend(handles=[midas_line, echo_line], loc='best')
# plt.legend(handles=[midas_line, echo_line], loc='lower right')
plt.legend(handles=[midas_line, echo_line], loc='upper right')

plt.savefig("plot1.png")
plt.show()

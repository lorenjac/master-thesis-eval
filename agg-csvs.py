from os import walk
import sys
import re

filename1 = sys.argv[1]
filename2 = sys.argv[2]

storename1 = re.findall('/(\w+)-', filename1)[0]
# print 'storename1 =', storename1

storename2 = re.findall('/(\w+)-', filename2)[0]
# print 'storename2 =', storename2

file1 = open(filename1, 'r')
lines1 = file1.readlines()
file1.close()

file2 = open(filename2, 'r')
lines2 = file2.readlines()
file2.close()

header = 'store;' + lines1[0]
print header[:-1]

values1 = storename1 + ';' + lines1[1]
values2 = storename2 + ';' + lines2[1]

print values1
print values2

import subprocess as subproc

target = './hello'
args = ['out there']

#subproc.call([target])
#subproc.call([target] + args)

#proc = subproc.Popen([target] + args)
proc = subproc.Popen([target] + args, stdout=subproc.PIPE)

while True:
  line = proc.stdout.readline()
  if line != '':
    print "test:", line.rstrip()
  else:
    break

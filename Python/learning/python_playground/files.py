import os

cmd = "dir"

fp = os.popen(cmd)
result = fp.read()
print result

stat = fp.close()
print stat

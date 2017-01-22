from producer import dummy
from producer import runcmd
from producer import vmstat
from producer import iostat
from producer import zonestat
from producer import dlstat
from producer import readfile

# stat = dummy.get_stream()

'''
cmd = ['/usr/bin/vmstat', '1']
stat = runcmd.get_stream(cmd, 1)
'''

#stat = vmstat.get_stream()
#stat = iostat.get_stream()
#stat = zonestat.get_stream()
#stat = dlstat.get_stream()
stat = readfile.get_stream()

period = stat['period']
stream = stat['stream']
print('the stat period is {0}'.format(period))
for _ in range(20):
    print(stream.readline())
stream.close()

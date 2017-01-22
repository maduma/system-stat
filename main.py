#from producer import dummy
#from producer import runcmd
#from producer import vmstat
#from producer import iostat
#from producer import zonestat
#from producer import dlstat
#from transformer import dummy
from producer import readfile
from transformer import dlstat

# stat = dummy.get_stream()

'''
cmd = ['/usr/bin/vmstat', '1']
stat = runcmd.get_stream(cmd, 1)
'''

#stat = vmstat.get_stream()
#stat = iostat.get_stream()
#stat = zonestat.get_stream()
#stat = dlstat.get_stream()

'''
period = stat['period']
stream = stat['stream']
print('the stat period is {0}'.format(period))
'''

#stream = dummy.get_transformer(stat)

stat = readfile.get_stream()
stream = dlstat.get_transformer(stat)
output = stream.readline()
for _ in range(45):
    print(output.next())
stream.close()

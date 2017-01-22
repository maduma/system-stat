import time
from chunker import dlstat

def get_transformer(producer):

    stream = producer['stream']
    period = producer['period']#
    chunker = dlstat.get_chunker(stream)

    class Dlstat:

        def readline(self):
            
            epoch = int(time.time())
            chunck = chunker.next()
            timestamp = chunck.pop(0).rstrip()
            for line in chunck:
                interface, rbytes, obytes = line.rstrip().split(':')
                # normalisation
                rbytes = int(rbytes) / period
                obytes = int(obytes) / period
                if '/' in interface: # zone vnic
                    zone, interface = interface.split('/')
                else:
                    zone = 'global'
                msg = '{0}.{1}.{{0}} {{1}} {2}'.format(zone, interface, timestamp)
                yield msg.format('rbytes', int(rbytes))
                yield msg.format('obytes', int(obytes))

        def close(self):
            stream.close()

    return Dlstat()

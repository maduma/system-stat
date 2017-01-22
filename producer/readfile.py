import time
import os

def get_stream():


    class FileStat:

        def __init__(self, filename):
            self.f = open(filename, 'r')
            self.nbr = 0

        def readline(self):
            self.nbr = self.nbr + 1
            yield self.f.readline()

        def close(self):
            print('{0} lines read'.format(self.nbr))
            self.f.close()

    period = 60 # seconds
    filename = 'dlstat.txt'
    directory = os.path.dirname(os.path.realpath(__file__))
    stream = FileStat(directory + os.path.sep + filename)

    return {'period': period, 'stream': stream}

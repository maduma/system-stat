import time
import os

def get_stream():


    class FileStat:

        def __init__(self, filename):
            self.f = open(filename, 'r')

        def readline(self):
            return self.f.readline()

        def close(self):
            self.f.close()

    period = 60 # seconds
    filename = 'dlstat.txt'
    directory = os.path.dirname(os.path.realpath(__file__))
    stream = FileStat(directory + os.path.sep + filename)

    return {'period': period, 'stream': stream}

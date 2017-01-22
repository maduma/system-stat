import time

def get_stream():

    class DummyStat:
        def readline(self):
            time.sleep(1)
            return 'this is memory stat line with this value -> 1224\n'
        def close(self):
            print('Closing dummy stat')

    period = 60 # seconds
    stream = DummyStat()

    return {'period': period, 'stream': stream}

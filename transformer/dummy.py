import time

def get_transformer(producer):

    stream = producer['stream']

    class Dummy:

        def readline(self):
            line = stream.readline()
            epoch = int(time.time())
            return 'dummy 123 ' + str(epoch)

        def close(self):
            stream.close()

    return Dummy()

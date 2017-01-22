# return chunk of x lines
# return an iterator
import re

def get_chunker(stream):

    timestamp = re.compile('^\d{10}$')
    chunck = []
    it = stream.readline()

    while True:
        line = it.next()
        if timestamp.match(line) and chunck:
            # timestamp line but not the first line
            yield chunck
            chunck = [line]
        else:
            chunck.append(line)

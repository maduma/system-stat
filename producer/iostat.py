import runcmd

def get_stream():
    cmd = ['/usr/bin/iostat', '-xnz', '1']
    return runcmd.get_stream(cmd, 1)

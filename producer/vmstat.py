import runcmd

def get_stream():
    cmd = ['/usr/bin/vmstat', '1']
    return runcmd.get_stream(cmd, 1)

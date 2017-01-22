import runcmd

def get_stream():
    cmd = ['/usr/bin/zonestat', '-p', '1']
    return runcmd.get_stream(cmd, 1)

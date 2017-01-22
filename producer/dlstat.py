import runcmd

def get_stream():
    cmd = ['/usr/sbin/dlstat'
        ,'-p', '-o', 'link,rbytes,obytes', '-T', 'u', '1']
    return runcmd.get_stream(cmd, 1)

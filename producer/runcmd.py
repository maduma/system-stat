import subprocess

def get_stream(cmd, period):

    class RunCmdStat:

        def __init__(self, cmd):
            self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        def readline(self):
            return self.p.stdout.readline()

        def close(self):
            self.p.kill()

    stream = RunCmdStat(cmd)
    return {'period': period, 'stream': stream}

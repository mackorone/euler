from glob import glob
from os import devnull
from subprocess import call
from sys import stdout
from time import time


def print_times(stream):
    null = open(devnull, 'w')
    for f in sorted(glob('[0-9][0-9][0-9].py')):
        stream.write(f)
        stream.flush()
        start = time()
        call(['python3.5', f], stdout=null, stderr=null)
        duration = format(time() - start, '.3f')
        stream.write(' - {}\n'.format(duration))


if __name__ == '__main__':
    print_times(stdout)

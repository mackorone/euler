from glob import glob
from json import loads
from subprocess import (
    PIPE,
    Popen,
)
from sys import (
    argv,
    stdout,
)
from time import time


def color(string, value):
    template = '\033[{}m'
    return '{}{}{}'.format(
        template.format(value),
        string,
        template.format(0),
    )


def check(filenames, stream):

    answers = loads(open('answers.txt').read())
    fail_mark = color(u'\u2717', 31)
    pass_mark = color(u'\u2714', 32)

    for filename in filenames:

        stream.write(filename)
        stream.flush()

        start = time()
        process = Popen(['python3.5', filename], stdout=PIPE)
        end = time()

        try:
            answer = int(process.communicate()[0])
        except ValueError:
            answer = None
        correct_answer = answers.get(filename)
        stream.write(' - {}'.format(
            pass_mark
            if answer is not None and answer == correct_answer
            else fail_mark
        ))

        duration = format(time() - start, '.3f')
        stream.write(' - {}\n'.format(duration))


if __name__ == '__main__':
    
    if 1 < len(argv):
        filenames = argv[1:]
    else:
        filenames = sorted(glob('[0-9][0-9][0-9].py'))

    check(filenames, stdout)

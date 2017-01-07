from enum import Enum
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


class Outcome(Enum):

    # NAME = (COLOR, SYMBOL)
    ERROR = (34, u'\u2049')
    FAILED = (31, u'\u2717')
    PASSED = (32, u'\u2714')

    @property
    def symbol(self):
        return color(self.value[1], self.value[0])

    @property
    def text(self):
        names = [x.name for x in list(Outcome)]
        max_length = max(len(x) for x in names)
        return color(self.name.ljust(max_length), self.value[0])


def check(answers, filenames, stream):

    results = {x: 0 for x in list(Outcome)}
    def count_result(outcome):
        results[outcome] += 1
        return outcome.symbol

    for filename in filenames:

        stream.write(filename)
        stream.flush()

        start = time()
        process = Popen(
            ['python3.5', filename],
            stdout=PIPE,
            stderr=PIPE,
        )

        try:
            answer = int(process.stdout.read())
        except ValueError:
            answer = None
        correct_answer = answers.get(filename)

        if answer is None or correct_answer is None:
            symbol = count_result(Outcome.ERROR)
        elif answer == correct_answer:
            symbol = count_result(Outcome.PASSED)
        else:
            symbol = count_result(Outcome.FAILED)
        stream.write(' - {}'.format(symbol))

        duration = str(time() - start)[:5]
        stream.write(' - {}\n'.format(duration))

    stream.write('-' * 18 + '\n')
    for outcome in [
        Outcome.PASSED,
        Outcome.FAILED,
        Outcome.ERROR,
    ]:
        stream.write('{} - {}\n'.format(
            outcome.text,
            results[outcome],
        ))


if __name__ == '__main__':
    
    try:
        answers = loads(open('answers.txt').read())
    except FileNotFoundError:
        answers = {}

    if 1 < len(argv):
        filenames = argv[1:]
    else:
        filenames = sorted(glob('[0-9][0-9][0-9].py'))

    check(answers, filenames, stdout)

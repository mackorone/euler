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
        return color(self.name, self.value[0])


def check(answers, filenames, stream):

    separator = ' - '
    duration_length = 5
    max_file_length = max(len(x) for x in filenames)

    results = {x: [0, 0.0] for x in list(Outcome)}
    def count_result(outcome, duration):
        results[outcome][0] += 1
        results[outcome][1] += duration
        return outcome.symbol

    for filename in filenames:

        # Write the filename
        stream.write(filename.ljust(max_file_length))
        stream.flush()

        # Run the problem
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
        duration = time() - start

        # Print the symbol
        correct_answer = answers.get(filename)
        if answer is None or correct_answer is None:
            symbol = count_result(Outcome.ERROR, duration)
        elif answer == correct_answer:
            symbol = count_result(Outcome.PASSED, duration)
        else:
            symbol = count_result(Outcome.FAILED, duration)
        stream.write(separator + symbol)

        # Print the duration and newline
        stream.write(separator + str(duration)[:duration_length])
        stream.write('\n')

    # Print a dashed line separating results from outcome totals
    stream.write('-' * (
        max_file_length +
        2 * len(separator) +
        1 + # len(symbol)
        duration_length
    ) + '\n')

    # Print outcome totals
    max_outcome_length = max(len(x.name) for x in list(Outcome))
    total_num_outcomes = sum(x[0] for x in results.values())
    for outcome in [
        Outcome.PASSED,
        Outcome.FAILED,
        Outcome.ERROR,
    ]:
        stream.write('{} - {} - {}\n'.format(
            outcome.text + ' ' * (max_outcome_length - len(outcome.name)),
            str(results[outcome][0]).rjust(len(str(total_num_outcomes))),
            "{:.10f}".format(results[outcome][1])[:duration_length],
        ))

    # Print a dashed line separating outcome totals from absolute totals
    stream.write('-' * (
        max_outcome_length +
        2 * len(separator) +
        len(str(total_num_outcomes)) +
        duration_length
    ) + '\n')

    # Print absolute totals
    stream.write('{} - {} - {}\n'.format(
        'TOTAL'.ljust(max_outcome_length),
        total_num_outcomes,
        str(sum(x[1] for x in results.values()))[:duration_length],
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

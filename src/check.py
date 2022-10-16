from datetime import datetime
from enum import Enum
from glob import glob
from json import loads
from files import (
    filename,
    filepath,
)
from subprocess import (
    PIPE,
    Popen,
)
from sys import (
    argv,
    stdout,
)
from time import time


class Outcome(Enum):

    # NAME = (COLOR, SYMBOL)
    ERROR = (34, u'\u2049')
    FAIL = (31, u'\u2717')
    PASS = (32, u'\u2714')

    @property
    def symbol(self):
        return color(self.value[1], self.value[0])

    @property
    def text(self):
        return color(self.name, self.value[0])


def color(string, value):
    template = '\033[{}m'
    return '{}{}{}'.format(
        template.format(value),
        string,
        template.format(0),
    )


def format_duration(duration):
    return datetime.fromtimestamp(duration).strftime('%M:%S.%f')[:9]


def check(answers, paths, stream):

    max_file_length = max(len(x) for x in paths)

    separator = ' - '
    format_string = '%06.3f' # total length of 6
    max_line_length = max_file_length + 2 * len(separator) + 7

    results = {x: [0, 0] for x in list(Outcome)}
    def count_result(outcome, duration):
        results[outcome][0] += 1
        results[outcome][1] += duration
        return outcome.symbol

    for path in paths:

        # Write the path
        stream.write(path.ljust(max_file_length))
        stream.flush()

        # Run the problem
        start = time()
        process = Popen(
            ['python3.5', path],
            stdout=PIPE,
            stderr=PIPE,
        )
        try:
            answer = int(process.stdout.read())
        except ValueError:
            answer = None
        duration = time() - start

        # Print the symbol
        correct_answer = answers.get(filename(path))
        if answer is None or correct_answer is None:
            symbol = count_result(Outcome.ERROR, duration)
        elif answer == correct_answer:
            symbol = count_result(Outcome.PASS, duration)
        else:
            symbol = count_result(Outcome.FAIL, duration)
        stream.write(separator + symbol)

        # Print the duration and newline
        stream.write(separator + format_string % duration + '\n')

    # Determine some line lengths for pretty-printing
    max_outcome_length = max(len(x.name) for x in list(Outcome))
    total_num_outcomes = sum(x[0] for x in results.values())
    outcomes_line_length = (
        max_outcome_length +
        2 * len(separator) +
        len(str(total_num_outcomes)) +
        len(format_duration(time()))
    )

    # Print a dashed line separating results from outcome totals
    stream.write('-' * max(max_line_length, outcomes_line_length) + '\n')

    # Print outcome totals
    for outcome in [
        Outcome.PASS,
        Outcome.FAIL,
        Outcome.ERROR,
    ]:
        stream.write('{} - {} - {}\n'.format(
            outcome.text + ' ' * (max_outcome_length - len(outcome.name)),
            str(results[outcome][0]).rjust(len(str(total_num_outcomes))),
            format_duration(results[outcome][1]),
        ))

    # Print a dashed line separating outcome totals from absolute totals
    stream.write('-' * outcomes_line_length + '\n')

    # Print absolute totals
    stream.write('{} - {} - {}\n'.format(
        'TOTAL'.ljust(max_outcome_length),
        total_num_outcomes,
        format_duration(sum(x[1] for x in results.values())),
    ))


if __name__ == '__main__':

    try:
        answers = loads(open(filepath('answers.txt')).read())
    except FileNotFoundError:
        answers = {}

    if 1 < len(argv):
        paths = argv[1:]
    else:
        paths = sorted(glob(filepath('[0-9][0-9][0-9].py')))

    check(answers, paths, stdout)

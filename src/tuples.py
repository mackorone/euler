from itertools import count


def gen_tuples(dimensions=2, duplicates=False, start=1):

    def helper(end, dims, acc):
        if dims == 1:
            yield acc
        else:
            for i in range(start, end + int(duplicates)):
                for value in helper(i, dims - 1, acc + (i,)):
                    yield value

    for i in count(start):
        for value in helper(i, dimensions, (i,)):
            yield value

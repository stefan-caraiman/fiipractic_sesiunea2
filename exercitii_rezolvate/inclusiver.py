"""Inclusive range test."""
from __future__ import print_function


class InclusiveRange:
    """Inclusive range class."""

    def __init__(self, *args):
        """Initialization of the class."""
        numargs = len(args)
        if numargs < 1:
            raise TypeError('Requires at least one argument.')
        elif numargs == 1:
            self._stop = args[0]
            self._start = 0
            self._step = 1
        elif numargs == 2:
            (self._start, self._stop) = args
            self._step = 1
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError('Function takes 3 arguments, {0} given'.format(numargs))

    def __iter__(self):
        """Make iterable object."""
        i = self._start
        while i <= self._stop:
            yield i
            i += self._step


def mainiter():
    """Run if module is called as main."""
    obj = InclusiveRange(1, 15, 2)
    for i in obj:
        print(i, end=' ')

if __name__ == "__main__":
    mainiter()


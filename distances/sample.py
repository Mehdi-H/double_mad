from typing import Iterable


class Sample(list):
    def __init__(self, *args):
        list.__init__(self, *args)

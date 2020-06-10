import sys

class RecursionLimit:
    def __init__(self, limit):
        self.limit = limit
        self.cur_limit = sys.getrecursionlimit()

    def __enter__(self):#changes the recussion limit
        sys.setrecursionlimit(self.limit)

    def __exit__(self, exc_type, exc_value, exc_traceback):#Clean up operation
        sys.setrecursionlimit(self.cur_limit)
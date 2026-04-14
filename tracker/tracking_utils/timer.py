import time

class Timer(object):
    """A simple timer."""
    def __init__(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.
        self.duration = 0.
        self.state = 0
    def tic(self):
        # using time.time instead of time.clock because time time.clock
        # does not normalize for multithreading
        self.start_time = time.time()
        self.state = 1
    def toc(self, average=True):
        if self.state == 1:
            self.diff = time.time() - self.start_time
            self.total_time += self.diff
            self.calls += 1
            self.average_time = self.total_time / self.calls
            if average:
                self.duration = self.average_time
            else:
                self.duration = self.diff
        else:
            print("issue tic first to begin timer")
            self.duration = 0.
        return self.duration
    def clear(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.
        self.duration = 0
        self.state = 0

import time

class TokenBucket():
    def __init__(self, capacity=5, last_consumed_time=None, fill_rate=1):
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.tokens = capacity
        self.timestamp = time.time() if last_consumed_time is None else last_consumed_time

    def consume(self, tokens):
        current_time = time.time()
        elapsed = current_time - self.timestamp
        self.tokens = min(self.capacity, self.tokens + elapsed * self.fill_rate)
        self.timestamp = current_time

        if tokens <= self.tokens:
            self.tokens -= tokens
            return True
        else:
            return False
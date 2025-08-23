import time

class CLK:
    def __init__(self, perido=1):
        self.state = 0
        self.perido = perido
        self.ultimo = time.time()

    def tick(self):
        now = time.time()
        if now - self.ultimo >= self.perido:
            self.state ^= 1  
            self.ultimo = now
        return self.state

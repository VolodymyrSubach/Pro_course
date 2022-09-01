class DigitalCounter:

    def __init__(self, start=0, end=100, current=None):
        if start < end:
            self.start = start
            self.end = end
        else:
            raise ValueError('Start point can not be more when End point!')
        if current is None or current < start or current > end:
            self.current = self.start
        else:
            self.current = current

    def increase(self, step=1):
        if self.current < self.end:
            self.current += step
        else:
            self.current = self.start

    def reset(self):
        self.current = self.start

    def get_current_value(self):
        return self.current

    def __str__(self):

        return f'min value = {self.start}, max value = {self.end}, current = {self.current}'


DigitalCounter(2, 100, 4)






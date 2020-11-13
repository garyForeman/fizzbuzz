class FizzBuzz:
    def parse(self, i):
        if i == 5:
            return 'buzz'
        elif i % 3 == 0:
            return 'fizz'
        else:
            return i
class FizzBuzz:
    def parse(self, i):
        if i % 15 == 0:
            return 'fizzbuzz'
        elif i % 5 == 0:
            return 'buzz'
        elif i % 3 == 0:
            return 'fizz'
        else:
            return i
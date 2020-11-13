from fizzbuzz import FizzBuzz
from flask import Flask
app = Flask(__name__)
FB = FizzBuzz()


@app.route('/<int:i>')
def fizz_buzz(i):
    return f'{FB.parse(i)}\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

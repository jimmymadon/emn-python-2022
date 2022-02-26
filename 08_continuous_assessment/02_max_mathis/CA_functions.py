def hello():
    name = str(input('Enter your name: '))
    print('Hello', name)


class Bank_transfer:
    def car(duration):
        return 500 * duration

    def home(duration):
        return 1000 * duration

    def mobile(duration):
        return 10 * duration * 12


class PayPal:
    def car(duration):
        return 500 * duration + (500 * duration * 0.1)

    def home(duration):
        return 1000 * duration + (1000 * duration * 0.1)

    def mobile(duration):
        return 10 * duration * 12 + (10 * duration * 0.1 * 12)


class Credit_card:
    def car(duration):
        return 500 * duration + (500 * duration * 0.2)

    def home(duration):
        return 1000 * duration + (1000 * duration * 0.2)

    def mobile(duration):
        return 10 * duration * 12 + (10 * duration * 0.2 * 12)

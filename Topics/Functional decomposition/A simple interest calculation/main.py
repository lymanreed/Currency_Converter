def calculate(amount, interest_rate, time):
    interest = amount * interest_rate * time / 100
    return interest, interest + amount


def print_result(interest, total_amount):
    print(f'The interest is: {interest}')
    print(f'The total amount is: {total_amount}')

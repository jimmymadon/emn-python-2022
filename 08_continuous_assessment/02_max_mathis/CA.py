import CA_functions
from numpy import average

CA_functions.hello()

# User enter its insurance policy in number of years
while True:
    duration_insurance = input(
        'Enter the duration of your insurance policy (years): ')
    if duration_insurance.strip().isdigit():
        print('Duration of your insurance in year(s):', duration_insurance)
        duration_insurance = int(duration_insurance)
        break
    else:
        print("Input is not a number. Please try again !")

# User choose its policy type: Car insurance, Home insurance or Mobile phone insurance
policy_type = ['Car insurance(1)', 'Home insurance(2)',
               'Mobile phone insurance(3)']

print('Choices: ', policy_type)
choose_policy = input('Choose a policy: ')
if choose_policy == '1':
    print('Your choice: Car insurance.')
elif choose_policy == '2':
    print('Your choice: Home insurance.')
elif choose_policy == '3':
    print('Your choice: Mobile phone insurance.')
else:
    print('Please, enter a valid option: 1; 2; 3.')


# User choose a payment type: Bank transfer, Paypal or Credit card
payment_type = ['Bank transfer(1)', 'PayPal(2)', 'Credit card(3)']
print('Payment type:', payment_type)
choose_payment = input('Choose a payment type: ')
if choose_payment == '1':
    print('Your choice: Bank transfer.')
elif choose_payment == '2':
    print('Your choice: PayPal.')
elif choose_payment == '3':
    print('Your choice: Credit card.')
else:
    print('Please, enter a valid option: 1; 2; 3.')

# Cost calculation
# Bank transfer
cost = 0
if choose_policy == '1' and choose_payment == '1':
    print('The cost of your insurance will be: ',
          CA_functions.Bank_transfer.car(duration_insurance))
elif choose_policy == '2' and choose_payment == '1':
    print('The cost of your insurance will be: ',
          CA_functions.Bank_transfer.home(duration_insurance))
elif choose_policy == '3' and choose_payment == '1':
    print('The cost of your insurance will be: ',
          CA_functions.Bank_transfer.mobile(duration_insurance))


# PayPal
if choose_policy == '1' and choose_payment == '2':
    print('The cost of your insurance will be: ',
          CA_functions.PayPal.car(duration_insurance))
elif choose_policy == '2' and choose_payment == '2':
    print('The cost of your insurance will be: ',
          CA_functions.PayPal.home(duration_insurance))
elif choose_policy == '3' and choose_payment == '2':
    print('The cost of your insurance will be: ',
          CA_functions.PayPal.mobile(duration_insurance))

# Credit card
if choose_policy == '1' and choose_payment == '3':
    print('The cost of your insurance will be: ',
          CA_functions.Credit_card.car(duration_insurance))
elif choose_policy == '2' and choose_payment == '3':
    print('The cost of your insurance will be: ',
          CA_functions.Credit_card.home(duration_insurance))
elif choose_policy == '3' and choose_payment == '3':
    print('The cost of your insurance will be: ',
          CA_functions.Credit_card.mobile(duration_insurance))

# List of Insurance premiums
insurance_premiums = []

while True:
    premiums = input(
        'Please enter your Insurance premiums (Type "q" to stop inputs and calculate premiums): ')
    if premiums == 'q':
        break
    insurance_premiums.append(float(premiums))

print(insurance_premiums)
sum_premiums = sum(insurance_premiums)
max_premiums = max(insurance_premiums)
average_premiums = average(insurance_premiums)

print('Sum of premiums: ', sum_premiums)
print('Maximum of premiums: ', max_premiums)
print('Average of premiums: ', average_premiums)

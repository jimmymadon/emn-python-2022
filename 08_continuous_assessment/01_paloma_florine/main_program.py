# We will model the basic functionality of an Insurance company such as Admiral (www.admiral.com). 
# System description / requirements :
# A user can create an Insurance Policy using your app. The user can enter the following policy details:
# User’s name
# Duration of Insurance Policy  in number of years
# Policy type: Car insurance, Home insurance or Mobile phone insurance
# Payment type: Bank transfer, PayPal or Credit card.

# The base ‘premium’ of the policy (cost of the insurance policy) needs to be calculated and is based on the type and duration. 
# Car Insurance = £500 per year.
# Home Insurance = £1000 per year.
# Mobile Phone Insurance = £10 per month.

# There is a transaction fee that is added to the base premium based on the payment type:
# Bank transfer = 0% (no fee)
# PayPal = 10% of the base premium.
# Credit Card = 20% of the base premium 
#  Write a Python program that allows the user to enter all the policy details as mentioned.
# Then calculate the total cost of the Insurance Policy for the entire duration of the policy. 
# Print all the details of the Policy nicely along with the total cost calculated above.
# Then, allow the user to enter a list of Insurance premiums (a series of float numbers). Neatly print the sum of these premiums, the value of the maximum premium entered and the average of all premiums entered.

# Hints and tips:
# You can write the whole program without using functions. But see if you can use a separate module(s) and re-usable functions within them to achieve the above tasks. 
import functions_CA

list_type_insurance=["Car Insurance","Home Insurance", "Mobile Phone"]
list_payment_name=["Bank transfer","PayPal","Credit Card"]

user=functions_CA.get_user_name()       # ask the user's name 
duration=int(functions_CA.get_duration_insurance())       # ask the duration
type_insurance=functions_CA.get_policy_type()           #ask the policy
payment_number=functions_CA.get_payment_type()          #ask the payment method 

name_payment=list_payment_name[int(payment_number)-1]            #return the chosen payment method
payment_percentage=functions_CA.get_percentage_payment_type(payment_number)     #return the payment fees
name_type_insurance=list_type_insurance[int(type_insurance)-1]            #return the chosen policy
price_type_insurance=int(functions_CA.get_price_type_insurance(type_insurance))       #return the price 
total_cost_insurance=(price_type_insurance+price_type_insurance*int(payment_percentage))*duration        #compute the final cost

print()
print("Hello", user, "!")
print("You selected", name_type_insurance, "policy and", name_payment, "as a payment method")
print("The total cost of your" ,duration,"years insurance is : £", total_cost_insurance)

# Function to return the name 
def get_user_name():
    name=(input("Please enter your name : "))
    return name 
# Function to return the duration
def get_duration_insurance():
    duration=input("Please enter the duration of your insurance : ")
    while True: 
        try:
            duration = int(duration)         #Integer value
            break

        except ValueError:
            duration=int(input("Invalid duration ! Please enter the duration of your insurance : "))   #Error message     
        if (duration<1 or duration> 100):                 #Between 1 and 100 years 
            duration=int(input("Invalid duration! Please enter the duration of your insurance :"))      
        else:
            break

    return duration
# Function to return the chosen policy
def get_policy_type():
    print("""Press :
    1: Car insurance
    2: Home insurance 
    3: Mobile phone insurance""")
    chosen_operation = input("Enter a number from the above menu: ")
    valid_chosen_operation=get_verification_menu(chosen_operation)
    return valid_chosen_operation
# Function to return the price of the chosen policy
def get_price_type_insurance(chosen_operation_insurance):      
    if chosen_operation_insurance==1:
        price_insurance=500
    elif chosen_operation_insurance==2:
        price_insurance=1000
    elif chosen_operation_insurance==3:
        price_insurance=10*12
    
    return price_insurance  

# Function to return the chosen payment method 
def get_payment_type():
    print("""Press :
    1: Bank transfer
    2: PayPal  
    3: Credit card""")
    chosen_operation = input("Enter a number from the above menu: ")
    valid_chosen_operation=get_verification_menu(chosen_operation)
    return valid_chosen_operation
# Function to return the percentage of fees applied according to the payment method 
def get_percentage_payment_type (name_payment):        
    if name_payment==1:
        percentage=0.0
    elif name_payment==2:
        percentage=0.1
    elif name_payment==3:
        percentage=0.2     
    return percentage    
# Function to verify the validity of a number typed by user (policy type, payment type)
def get_verification_menu(chosen_operation):
    while True: 
        try:
            chosen_operation = int(chosen_operation)
            break
        except ValueError:
            chosen_operation=input("Invalid ! Enter a number from the above menu: ")
        chosen_operation=int(chosen_operation)  
          
        if (chosen_operation < 1 or chosen_operation > 3):
            chosen_operation = input("Invalid ! Enter a valid number from the above menu: ")
        else: 
            chosen_operation=int(chosen_operation)
            break

    return chosen_operation 
# Description : One  Stop  Insurance  Company  program  to  enter  and  calculate  new  insurance  policy information for its customers.
# Author : Michael O'brien
# Dates : March 21 - 24 , 2024

import datetime

# Default values
NEXT_POLICY_NUM = 1944
BASIC_PREMIUM = 869.00
DISC_ADD_CARS = 0.25
COST_EXTRA_LIABILITY = 130.00
COST_OF_GLASS = 86.00
COST_LOAN_CAR = 58.00
HST_RATE = 0.15
PROCESS_FEE = 39.99

# List of valid provinces
valid_provinces = ['ON', 'QC', 'NS', 'NB', 'MB', 'BC', 'PE', 'SK', 'AB', 'NL']

# Lists to store previous claims
ClaimNumList = []
ClaimDatesList = []
ClaimAmntList = []

# Function to validate province input
def validate_province(Province):
    return Province in valid_provinces

# Function to validate date input
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to calculate insurance premium
def calculate_premium():
    TotalPrem = BASIC_PREMIUM + (NumCars - 1) * BASIC_PREMIUM * DISC_ADD_CARS
    ExtraCosts = 0
    if ExtraLib == 'Y':
        ExtraCosts += NumCars * COST_EXTRA_LIABILITY
    if GlassCov == 'Y':
        ExtraCosts += NumCars * COST_OF_GLASS
    if LoanCar == 'Y':
        ExtraCosts += NumCars * COST_LOAN_CAR
    TotalPrem += ExtraCosts
    return TotalPrem

# Function to calculate total cost
def calculate_total_cost():
    TotalCost = Premium + (Premium * HST_RATE) + PROCESS_FEE
    return TotalCost

# Function to calculate monthly payment
def calculate_monthly_payment(totalcost, downpayment=0):
    monthlypayment = (totalcost - downpayment + PROCESS_FEE) / 8
    return monthlypayment

# Function to display claims
def display_claims():
    print("---------------------------------")
    print("Claim #   Claim Date    Amount")
    print("---------------------------------")
    for i in range(len(ClaimNumList)):
        print(f"{ClaimNumList[i]}    {ClaimDatesList[i]}    ${ClaimAmntList[i]:,.2f}")


while True:
    # Customer information input
    FirstName = input("Enter customer's first name: ").title()
    LastName = input("Enter customer's last name: ").title()
    Address = input("Enter customer's address: ")
    City = input("Enter city: ").title()
    Province = input("Enter province (2-letter code): ").upper()
    while not validate_province(Province):
        Province = input("Enter a valid province (2-letter code): ").upper()
    PostCode = input("Enter postal code: ")
    PhoNum = input("Enter phone number: ")
    NumCars = int(input("Enter number of cars being insured: "))
    ExtraLib = input("Extra liability coverage? (Y/N): ").upper()
    GlassCov = input("Glass coverage? (Y/N): ").upper()
    LoanCar = input("Loaner car coverage? (Y/N): ").upper()
    PayMethod = input("Payment method (Full/Monthly/Down Pay): ").title()
    if PayMethod == 'Down Pay':
        DownPay = float(input("Enter down payment amount: "))
    else:
        DownPay = 0
    
    # Claims input
    while True:
        claim_number = input("Enter claim number (press Enter to skip): ")
        if not claim_number:
            break
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        while not validate_date(claim_date):
            claim_date = input("Enter a valid claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        ClaimNumList.append(claim_number)
        ClaimDatesList.append(claim_date)
        ClaimAmntList.append(claim_amount)
        
    # Calculate premium and total cost
    Premium = calculate_premium()
    TotalCost = calculate_total_cost()
    MonthlyPay = calculate_monthly_payment(TotalCost, DownPay) 
    
    # Display receipt
    print("\n=================================================")
    print("                  Receipt                      ")
    print("=================================================")
    print(f"Date: {datetime.date.today()}\n")

    print("Customer Information:")
    print("----------------------------------")
    print(f"Name: {FirstName} {LastName}")
    print(f"Address: {Address}")
    print(f"City: {City}, Province: {Province}, Postal Code: {PostCode}")
    print(f"Phone Number: {PhoNum}\n")

    print("Insurance Details:")
    print("----------------------------------")
    print(f"Number of Cars Insured: {NumCars}")
    print(f"Extra Liability Coverage: {ExtraLib}")
    print(f"Glass Coverage: {GlassCov}")
    print(f"Loaner Car Coverage: {LoanCar}")
    print(f"Payment Method: {PayMethod}")
    if PayMethod == 'Down Pay':
        print(f"Down Payment Amount: ${DownPay:<,.2f}")

    print("\nCost Summary:")
    print("----------------------------------")
    print(f"Total Insurance Premium: ${Premium:<,.2f}")
    print(f"Total Cost (incl. HST): ${TotalCost:<,.2f}")
    print(f"Monthly Payment: ${MonthlyPay:<,.2f}")

    print("\nFirst Payment Date:")
    print("----------------------------------")
    print(datetime.date.today().replace(day=1) + datetime.timedelta(days=32))
    print("=================================================")

    display_claims()
    
    NEXT_POLICY_NUM += 1
    print("Policy data has been saved.")
    print()
    if input("Do you want to enter another customer? (Y/N): ").upper() != 'Y':
        break

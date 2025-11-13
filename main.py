'''
You work for the tech department of your city, and another government department needs you to create a chatbot to help automate some 
of their common functions (you can choose dept and functions)
Ex - Dept of Motor Vehicles - Needs to help with registering car, sign up for license test, pay fees
Ex - Dept of Education - Helps families find schools nearby, applications, school holidays

Scenario 4 - Dept of Human Services
Need to ask for name
Need to provide different options to choose from
Options can include, SNAP, Housing Assistance, Unemployment, Welfare
For each option, will have sub-options like: Information, check your status, application, update information
Need to collect information like account # and pin
'''


# 1. Voter Registration Functions
def check_registration(): 
    full_name = input("\nEnter your full name: ")
    dob = input("Enter your date of birth: ")

    # Different selections the user can enter
    criteria1 = "1. County and Zip Code"
    criteria2 = "2. Driver's License"
    criteria3 = "3. Voter ID"
    print("\nNext, please choose from one of the following selection criteria: \n" + criteria1 + "\n" + criteria2 + "\n" + criteria3)
    choice = input("Enter your information: ")

    print("\nYour voter registration is currently ACTIVE.")

def new_registration():
    age = int(input("\nTo make sure you are eligible, please enter your age: "))
    if age < 18:
        print("Sorry you must be 18 to register to vote. You are currently only " + str(age) + ".")
    else:
        print("\nYou are eligible to vote. Please follow the instructions below.")
        full_name = input("Enter your full name: ")
        dob = input("Enter your date of birth (MM/DD/YYYY): ")
        address = input("Enter your address: ")
        print("\nThank you " + full_name + " for registering. You will recieve an official confirmation by mail.")

# 2. Mail-in Ballot Functions
def request_ballot():
    print("Voting by mail in Texas is limited to those who are: ")
    print("- 65 years or older")
    print("- Sick or disabled")
    print("- Expected to give birth within 3 weeks of Election Day")
    print("- Out of the county on Election day AND during the period for early voting")
    print("- Confined in jail, but otherwise eligible")
    user_input = input("\nDo any of the above options apply to you? (Y/N):")
    user_input = user_input.upper()
    if user_input == "Y":
        print("\nYou are eligible to vote by mail. Please follow the instructions below.")
        full_name = input("Enter your full name: ")
        dob = input("Enter your date of birth (MM/DD/YYYY): ")
        address = input("Enter your mailing address: ")
        print("Enter one of the following numbers below: driver's license, ID card, or election identification certificate")
        ID = input("Enter here: ")
        print("\nMail-in ballot sucessfully requested. Ballot will be mailed to " + address + ".\n")
    elif user_input == "N":
        print("\nYou are not eligible to vote by mail.\n")
        
def track_ballot():
    full_name = input("\nEnter your full name: ")
    dob = input("Enter your date of birth (MM/DD/YYYY): ")
    ssn = input("Enter the last 4 digits of SSN: ")
    ID = input("Enter driver's license number of DPS pin: ")
    print("\nStatus: Mailed - Estimated delivery: 3-5 business days.")

# 3. Polling Location Functions
def find_by_address():
    address = input("\nEnter your address: ")
    print("The closest location is 1.2 miles away: Austin Public Library.")

def view_early():
    print("\nList of Early Voting Locations: ")
    print("Austin City Hall \nAustin Energy Headquarters")
    print("Balcones Woods Shopping Center")
    print("Dan Ruiz Branch Library \nGeorge Morales Dove Springs Recreation Center")
    print("LBJ School of Public Affairs")
    print("Westminster Presbyterian Church\n")

def view_election_day():
    print("\nList of Election Day Locations: ")
    print("Community Center at Del Valle \nDel Valle ISD Admin Building")
    print("Elevate Event Center \nHendrickson High School \n PACE Campus Gym")
    print("Pleasant Hill Branch Library \nRiver Place Elementary \nSunset Valley City Hall\n")


print("Welcome to the Travis County Clerk's Office. \nI am Pol, a virtual assistant. How can I be of assistance?")
option1 = "1. Voter Registration"
option2 = "2. Mail-In Ballots"
option3 = "3. Polling Locations"
option4 = "4. Exit"

while True:
    assist = print("\nPlease choose from one of the following options: \n" + option1 + "\n" +
            option2 +"\n" + option3 + "\n" + option4)
    enter_option = input("\nEnter your choice (1-4): ")


    if enter_option == "1":
        while True:
            print("\n---- Voter Registration ----")
            print("1. Check Voter Registration Status")
            print("2. Start New Registration")
            print("3. Go Back to Main Menu")
            sub_option1 = input("\nEnter your choice (1-3): ")
            if sub_option1 == "1":
                check_registration()
            elif sub_option1 == "2":
                new_registration()
            elif sub_option1 == "3":
                break
            else:
                print("Invalid choice. Please try again")
    elif enter_option == "2":
        while True:
            print("---- Request a Mail-In Ballot ----")
            print("1. Request a Mail-In Ballot")
            print("2. Track your Ballot")
            print("3. Go Back to Main Menu")
            sub_option2 = input("\nEnter your choice (1-3): ")
            if sub_option2 == "1":
                request_ballot()
            elif sub_option2 == "2":
                track_ballot()
            elif sub_option2 == "3":
                break
            else:
                print("Invalid choice. Please try again")
    elif enter_option == "3":
        while True: 
            print("---- Polling Locations ----")
            print("1. Find by Address")
            print("2. View Early Voting Locations")
            print("3. View Election Day Locations")
            print("4. Go Back to Main Menu")
            sub_option3 = input("\nEnter your choice (1-3): ")
            if sub_option3 == "1":
                find_by_address()
            elif sub_option3 == "2":
                view_early()
            elif sub_option3 == "3":
                view_election_day()
            elif sub_option3 == "4":
                break
            else:
                print("Invalid choice. Please try again")
    elif enter_option == "4":
        print("\nYou have chosen to exit the chat. I hope I was of assistance. Goodbye!")
        exit()
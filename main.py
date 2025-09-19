print("Welcome to the Retail Store Chatbox!")
name = input("What is your name? ")
age = input("Hello " + name + ". How old are you? ")
print("\nHow can I help you today?")

option1 = "1. Placeholder"
option2 = "2. Placeholder"
option3 = "3. Placeholder"
option4 = "4. Exit the chat"
assist = print("I can assist you with one of the following options below: \n" + option1 + "\n" +
           option2 +"\n" + option3 + "\n" + option4 + " ")
enter_option = input("Please enter a number to pick an option: ")

if enter_option == "1":
    print("Response1")
elif enter_option == "2":
    print("Response2")
elif enter_option == "3":
    print("Response3")
elif enter_option == "4": 
    print("You have chosen to exit the chat. I hope I was of assistance. Goodbye!")
    exit()

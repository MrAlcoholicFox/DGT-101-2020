################################################################################
#todo list
##Fix validation for computer_choice
##Make it so that entering integer in user_last_name or user_first_name says something
################################################################################

#Dictionary and lists which contain info for the code to use
#computer_type_and_price = {900: "Home Basic", 1200: "Office", 1500: "Gamer", 2200: "Studio"}
#computer_type_and_price = [["Home Basic", 900], ["Office", 1200], ["Gamer", 1500], ["Studio", 2200]]
computer_type = ["Home Basic", "Office", "Gamer", "Studio"]
computer_price = [900, 1200, 1500, 2200]
computer_ram_list = [4, 8, 16, 16]
computer_graphics_list = ["Built In", "Built In", "4GB Nvidia", "4GB Quadro"]
computer_monitors_list = ["20", "23", "27", "Dual 23"]
#defining the banner Function
def banner():
    print("""

  |||                   |||                 |||                                     |
    |    |              ||                 |   |                                    |
    |                  |                   |                                        |
    |   ||    | | ||          ||||         |       ||||   | | ||   | |||   |    |  ||||    ||||   | ||
    |    |    || |  |        |    |        |      |    |  || |  |  ||   |  |    |   |     |    |   |
    |    |    |  |  |         ||           |      |    |  |  |  |  |    |  |    |   |     ||||||   |
    |    |    |  |  |           ||         |      |    |  |  |  |  ||   |  |    |   |     |        |
|   |    |    |  |  |        |    |        |   |  |    |  |  |  |  | |||   |   ||   |  |  |    |   |
 |||   |||||  |  |  |         ||||          |||    ||||   |  |  |  |        ||| |    ||    ||||    |
                                                                   |
                                                                   |

""")

#Defining the menu function
def menu():
    #The main menu where the user chooses the option which then raises the function specified
    global mode
    while True:
        try:
            mode = int(input("""Please enter a number corresponding to the mode:
            1: Order
            2: Computer Types And Prices
            3: Computer Specs
            """))
            return mode
            #validation
        except ValueError:
            print("No number was entered, please try again")
            print("")


#defining the order function
def order(compter_type, computer_price):
    
    #gets input from user for their first name and then validates it by te
    #it also prevents from users entering a value less than 2 letters long
    user_first_name = ""
    while user_first_name.isalpha() != True:
        user_first_name = input("What is your first name? ").strip()
        if len(user_first_name) < 2:
            print("Please enter a first name with more than one letter")
            user_first_name = ""
        elif user_first_name.isdigit() == True:
            print("Please enter letters and not numbers!")
            user_first_name = ""

    #Gets input from user for their last name and then validates it
    user_last_name = ""
    while user_last_name.isalpha() != True:
        user_last_name = input("What is your last name? ").strip()
        if len(user_last_name) < 3 and len(user_last_name) > 0:
            print("Please enter a last name with more than two letters")
            user_last_name = ""
        elif len(user_last_name) == 0:
            print("Please enter your last name and don't leave it blank")
            user_last_name = ""
        elif user_last_name.isdigit() == True:
            print("Please enter letters and not numbers!")

    #Get input from the user for their age and then validates it
    while True:
        try:
            user_age = int(input("What is your age? "))
            if user_age < 13 or user_age > 110:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please Enter A Numerical Value Or Something Between The Age Boundaries of 13 - 110")

    #get input from the user for what computer type they want and then validate
    global computer_choice
    while True:
        try:
            computer_choice = "None"
            while computer_choice not in computer_price:
                computer_choice = int(input("How much does the computer that you want cost? "))
                print("")
                if computer_choice not in computer_price:
                    print("Please enter the price of one of our computers")
                elif computer_choice in computer_price:
                    break
            break
        except ValueError:
            print("Please enter a numerical value")

    #gets input from user for how much money they have and then validate it
    global user_money
    while True:
        try:
            user_money = int(input("How much money do you have? "))
            if user_money < 0:
                raise ValueError
            else:
                print("")
                break
        except ValueError:
            print("Please Enter A Numerical Value")

    #if statements to decide what should happen
    if user_money >= computer_choice:
        print("Congratulations {} {}, You can afford the ${} setup".format(user_first_name, user_last_name, computer_choice))
        print("The total cost will be ${}, and your change will be ${}".format(computer_choice, (user_money - computer_choice)))
        while True:
            user_confirmation = input("Is this want you want (yes or no) ").lower().strip()
            #Order Confirmed
            if user_confirmation == "yes" or user_confirmation == "y":
                print("Thank you {} {} for your purchase".format(user_first_name, user_last_name))
                break
            #order Aborted
            elif user_confirmation == "no" or user_confirmation == "n":
                print("Order aborted, Please come again")
                break
            #validation
            else:
                print("Please enter yes or no")

    #If statement for if the user cannnot get finance because they are under 18
    elif user_money < computer_choice and user_age < 18:
        print("Sorry But You Cannot Afford The Setup That You Want And Since You Are Under 18 We Cannot Offer You Finance So Keep Saving")

    #If statement for if the user can get finance because they are 18 or older
    elif user_money < computer_choice and user_age >= 18:
        print("Sorry But You Cannot Afford The Setup That You Want But Since You Are 18 Or Older If You Come In Store We Can Offer You Finance")

#defining the function that prints the computer setup names and their price
def computer_types(computer_type, computer_price):
    i = 0
    for i in range(len(computer_type)):
        print("The {} setup costs ${}".format(computer_type[i], computer_price[i]))
        print("")

#defining the function that prints the computers specs
def computer_specs(computer_type, computer_ram_list, computer_graphics_list, computer_monitors_list):
    i = 0
    for i in range(4):
        print("Computer Type: {} Setup | Computer Ram: {}GB | Graphics: {} Graphics | Monitor Size: {} Inches".format(computer_type[i], computer_ram_list[i], computer_graphics_list[i], computer_monitors_list[i]))
        print("")
        i += 1

#Main execution area
banner()
while True:
    menu()

    #execute order if chosen in the menu
    if mode == 1:
        order(computer_type, computer_price)
        break
    #execute the mode computer_types if chosen in the menu
    elif mode == 2:
        computer_types(computer_type, computer_price)

    elif mode == 3:
        computer_specs(computer_type, computer_ram_list, computer_graphics_list, computer_monitors_list)

    else:
        print("Please Choose One Of The Options")
        print("")
banner()

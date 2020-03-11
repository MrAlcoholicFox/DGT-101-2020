################################################################################
#todo list
##Maybe use dictionary instead of new list
#Make Validation
##check that pc choice is in list
################################################################################

#Dictionary and lists which contain info for the code to use
computer_type_and_price = {"Home Basic": 900, "Office": 1200, "Gamer": 1500, "Studio": 2200}
computer_type_list = ["Home Basic", "Office", "Gamer", "Studio"]
computer_ram_list = [4, 8, 16, 16]
computer_graphics_list = ["Built In", "Built In", "4GB Nvidia", "4GB Quadro"]
computer_monitors_list = ["20", "23", "27", "Dual 23"]
#defining the banner Function
def banner():
    print("""

  |||                                 |||                                     |
    |    |                           |   |                                    |
    |                                |                                        |
    |   ||    | | ||    ||||         |       ||||   | | ||   | |||   |    |  ||||    ||||   | ||   ||||
    |    |    || |  |  |    |        |      |    |  || |  |  ||   |  |    |   |     |    |   |    |    |
    |    |    |  |  |   ||           |      |    |  |  |  |  |    |  |    |   |     ||||||   |     ||
    |    |    |  |  |     ||         |      |    |  |  |  |  ||   |  |    |   |     |        |       ||
|   |    |    |  |  |  |    |        |   |  |    |  |  |  |  | |||   |   ||   |  |  |    |   |    |    |
 |||   |||||  |  |  |   ||||          |||    ||||   |  |  |  |        ||| |    ||    ||||    |     ||||
                                                             |
                                                             |
""")

#Defining the menu function
def menu():
    global mode
    while True:
        try:
            mode = int(input("""Please enter a number corresponding to the mode:
            1: Order
            2: Computer Types And Prices
            3: Computer Specs
            """))
            return mode
        except ValueError:
            print("No number was entered, please try again")
            print("")


#defining the order function
def order(computer_type_and_price):

    while True:
        try:
            user_name = input("What is your name? ")
            user_age = int(input("What is your age? "))
            global computer_choice
            computer_choice = "None"
            while computer_choice not in computer_type_and_price:
                computer_choice = input("""Please enter the name of the setup that you want;
                Home Basic
                Office
                Gamer
                Studio
                """).title()
                print("")
            global user_money
            user_money = int(input("How much money do you have? "))
            print("")
            break
        except ValueError:
            print("Please Enter A Number")
    #if statements to decide what should happen
    if user_money >= computer_type_and_price[computer_choice]:
        print("Congratulations {}, You can afford {}".format(user_name, computer_choice))
        print("The total cost will be ${}".format(computer_type_and_price[computer_choice]))
        while True:
            user_confirmation = input("Is this want you want (yes or no) ").lower().strip()
            if user_confirmation == "yes":
                print("Thank you {} for your purchase".format(user_name))
                break
            elif user_confirmation == "no":
                print("Order aborted, Please come again")
                break
            else:
                print("Please enter yes or no")
    elif user_money < computer_type_and_price[computer_choice] and user_age < 18:
        print("Sorry But You Cannot Afford The {} Setup And Since You Are Under 18 We Cannot Offer You Finance So Keep Saving".format(computer_choice))
    elif user_money < computer_type_and_price[computer_choice] and user_age >= 18:
        print("Sorry But You Cannot Afford The {} Setup, But Since You Are 18 Or Older If You Come In Store We Can Offer You Finance".format(computer_choice))

#defining the function that prints the computer setup names and their price
def computer_types(computer_type_and_price):
    for type, price in computer_type_and_price.items():
        print("The {} setup costs ${}".format(type, price))
        print("")

#defining the function that prints the computers specs
def computer_specs(computer_type_and_price, computer_type_list, computer_ram_list, computer_graphics_list, computer_monitors_list):
    i = 0
    for i in range(len(computer_type_and_price)):
        print("Computer Type: {} Setup | Computer Ram: {}GB | Graphics: {} Graphics | Monitor Size: {} Inches".format(computer_type_list[i], computer_ram_list[i], computer_graphics_list[i], computer_monitors_list[i]))
        print("")
        i += 1


banner()
while True:
    menu()

    #execute order if chosen in the menu
    if mode == 1:
        order(computer_type_and_price)
        break
    #execute the model types if chosen in the menu
    elif mode == 2:
        computer_types(computer_type_and_price)

    elif mode == 3:
        computer_specs(computer_type_and_price, computer_type_list, computer_ram_list, computer_graphics_list, computer_monitors_list)

    else:
        print("Please Choose One Of The Options")
        print("")

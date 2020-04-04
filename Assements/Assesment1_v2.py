################################################################################
#todo list
##Maybe use dictionary instead of new list | Can't see this working
#Make Validation | Completed
##check that pc choice is in list | No
##Maybe make less try and except? | Done
##make it so that negative values don't work | Done
##make it so that when the person is asked for the computer type and they put in-
##something wrong then print something telling them that they put it wrong. | Done
##Add validation for the name entry | done
##Add a last name | done
##Maybe make it so that when user denies order it takes them back to the menu
##Make more comments | pending
##Maybe make it so Y/N is a correct confirmation method | Done
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
    #The main menu where the user chooses the option
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
def order(computer_type_and_price):
    #gets input from user for their first name and then validates it
    #it also prevents from users entering a value less than 2 letters long
    user_first_name = ""
    while len(user_first_name) < 2:
        user_first_name = str(input("What is your first name? ")).strip()
        if len(user_first_name) < 2:
            print("Please enter your first name and don't leave it blank")

    #Gets input from user for their last name and then validates it
    user_last_name = ""
    while len(user_last_name) < 4:
        user_last_name = input("What is your last name? ").strip()
        if len(user_last_name) < 4:
            print("Please enter your last name and don't leave it blank")

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
    computer_choice = "None"
    while computer_choice not in computer_type_and_price:
        computer_choice = input("""Please enter the name of the setup that you want;
        Home Basic
        Office
        Gamer
        Studio
        """).title()
        print("")
        if computer_choice not in computer_type_and_price:
            print("Please choose one of the choices")

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
    if user_money >= computer_type_and_price[computer_choice]:
        print("Congratulations {} {}, You can afford {}".format(user_first_name, user_last_name, computer_choice))
        print("The total cost will be ${}, and your change will be ${}".format(computer_type_and_price[computer_choice], (user_money - computer_type_and_price[computer_choice])))
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
    elif user_money < computer_type_and_price[computer_choice] and user_age < 18:
        print("Sorry But You Cannot Afford The {} Setup And Since You Are Under 18 We Cannot Offer You Finance So Keep Saving".format(computer_choice))

    #If statement for if the user can get finance because they are 18 or older
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


#Main execution area
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
banner()

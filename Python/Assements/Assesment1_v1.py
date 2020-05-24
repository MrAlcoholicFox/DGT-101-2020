################################################################################
#Todo list
##maybe change name of choice funtion
##add validation
################################################################################

#lists and dictionaries
computer_type_and_price = {"Home Basic": 900, "Office": 1200, "Gamer": 1500, "Studio": 2200}

#defining the questions
def questions(computer_type_and_price):
    print("Welcome to Jim's computer place")
    user_name = input("What is your name? ")
    user_age = int(input("What is your age? "))
    global computer_choice
    computer_choice = input("""Please enter the name of the computer that you want;
    Home Basic: 900
    Office: 1200
    Gamer: 1500
    Studio: 2200
    """)
    global user_money
    user_money = int(input("How much money do you have? "))


#defining the choice function
def choice(computer_type_and_price):
    if user_money >= computer_type_and_price[computer_choice]:
        print("You can afford {}".format(computer_choice))
        



#running the code
questions(computer_type_and_price)
choice(computer_type_and_price)

################################################################################
#Todo list
##maybe change name of choice funtion
################################################################################

#lists and dictionaries
computer_type_and_price = {"Home Basic": 900, "Office": 1200, "Gamer": 1500, "Studio": 2200}

#defining the questions
def questions(computer_type_and_price):
    print("Welcome to Jim's computer place")
    user_name = input("What is your name? ")
    user_age = int(input("What is your age? "))
    global computer_price
    computer_price = int(input("""How much is the computer you want? (prices for reference)
    Home Basic: 900
    Office: 1200
    Gamer: 1500
    Studio: 2200
    """))
    user_money = int(input("How much money do you have? "))


#defining the choice function
def choice(computer_type_and_price):
    if computer_price >= 900 or computer_price < 1200:
        print("The only computer that you can afford is The Home Basic")
        print("Specs: RAM: 4GB RAM | Graphics: Built In Graphics | Monitor Size: 20 inches")




#running the code
questions(computer_type_and_price)


choice(computer_type_and_price)

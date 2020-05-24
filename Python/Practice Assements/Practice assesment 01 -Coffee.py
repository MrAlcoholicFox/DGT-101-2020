#todo list
##get a life
##add more comments
##make it so name can't be left empty
##Make it so if someone enters their name again they can update their order or they can just be refused the right to order
##make it so the person can order multiple types of coffee maybe
##Print the coffee machine thing
##make it so it is ovious to choose number for coffee choice

#Amount of coffees needed list
coffee_quantity = []

#Order dictionary
order_list = {}

#Coffee dictionary
coffee_list = {1: "flat white", 2: "decaf", 3: "latte", 4: "cappuccino", 5: "hot chocolate"}

#Defining total_coffee_order
def total_coffee_order(coffee_quantity, order_list, coffee_list):
    order_num = 1
    loop_quantity = 0
    for names, coffee in order_list.items():
        print("Order {}: Name: {} | Coffee Type: {} | Coffee Amount: {} ".format(order_num, names, coffee_list[coffee], coffee_quantity[loop_quantity]))
        order_num += 1
        loop_quantity += 1

#Defining banner
def banner():
    print("""

|||             |||     |||                          ||||                  ||||            |      |
|   |           |   |   |   |                        |    |                |    |           |      |
|               |       |                            |                     |                |      |
|       ||||    |       |       ||||    ||||         |        ||||         |        ||||   ||||   ||||    ||||   | ||   ||||
|      |    |  ||||    ||||    |    |  |    |        |       |    |        |       |    |   |      |     |    |   |    |    |
|      |    |   |       |      ||||||  ||||||        |  |||  |    |        |  |||  ||||||   |      |     ||||||   |     ||
|      |    |   |       |      |       |             |    |  |    |        |    |  |        |      |     |        |       ||
|   |  |    |   |       |      |    |  |    |        |   ||  |    |        |   ||  |    |   |  |   |  |  |    |   |    |    |
 |||    ||||    |       |       ||||    ||||          ||| |   ||||          ||| |   ||||     ||     ||    ||||    |     ||||

""")

#defining coffee choice function
def coffee_order(order_list, coffee_list):
    #set this while true to a while variable != f
    name = None
    while name != "F":
        coffee_choice = None
        order_confirmation = "peanuts"
        coffee_amount = False
        #maybe change name to a better named variable
        name = input("Please enter your name (F to finish): ").strip().title()
        if name == "F":
            print("Orders Completed")
            break

        elif name not in order_list:
            while coffee_choice not in coffee_list:
                try:
                    coffee_choice = int(input("""Please choose one of the following numbers for your drink:
                1: flat white
                2: decaf
                3: latte
                4: cappuccino
                5: hot chocolate
                """))
                except ValueError:
                    print("Please a numerical value ")
            while coffee_amount == False:
                try:
                    while True:
                        coffee_amount = int(input("How many {}'s do you want: ".format(coffee_list[coffee_choice])))
                        if coffee_amount <= 3 and coffee_amount > 0:
                            break
                        else:
                            print("Please enter a number from 1 to 3")
                except ValueError:
                    print("Please enter a numerical value")
            #confirms order
            print("Name: {} | Coffee Choice: {} | Coffee amount: {}".format(name, coffee_list[coffee_choice], coffee_amount))
            #maybe make it so the person can change it later
            order_confirmation = input("Are you happy with your order (yes or no) you can't change this later: ").strip().lower()
            #extreme branchy boi
            if order_confirmation == "yes" or "y":
                #puts the stuff into their lists and dicts
                print("Order completed, thank you")
                order_list[name] = coffee_choice
                coffee_quantity.append(coffee_amount)
            #for the no
            elif order_confirmation == "no" or "n":
                print("Aborting order")
                #I might change this later so this doesnt abort but for now I don't care
            else:
                print("Neither 'yes' or 'no' was entered, order aborted")

banner()
coffee_order(order_list, coffee_list)
total_coffee_order(coffee_quantity, order_list, coffee_list)
banner()

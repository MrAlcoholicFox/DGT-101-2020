######################################################################################################################################
#thoughts and to/dos
##I might need a cost list but probs not
##might need to make some variables global
######################################################################################################################################
name_and_egg_dict = {}
global_loop_variable = None
user_name = None
count = 0
def name_entry(name_and_egg_dict):
    while True:
        user_name = input("Please enter your name (F to finish) ").strip().title()
        break
    if user_name in name_and_egg_dict:
        global global_loop_variable
        global_loop_variable = "name in list"
        return global_loop_variable

    elif user_name == "F":
        global_loop_variable = "Summary"
        return global_loop_variable

    else:
        global_loop_variable = "new user"
        return global_loop_variable

def first_order(count):
    try:
        #add loop thingy
        order_amount = int(input("How many dozen eggs do you want? "))
        print("Hello {}, You ordered {} dozen eggs which means that your total cost is {}".format(user_name, order_amount, (order_amount * 6.5)))
    except ValueError:
        print("Please enter a number")

def confirmation(name_and_egg_dict):
    while True:
        confirm = input("Is this correct (yes or no) ").strip().lower()
        if confirm == "yes":
            print("Order Success, Updating Records")
            name_and_egg_dict[user_name] = order_amount
            break
        elif confirm == "no":
            print("Order Aborted")
            break
        else:
            print("please enter yes or no")

def returning_order(name_and_egg_dict):
    order_amount = int(input("Hello returning customer, how many more dozens eggs would you like? "))
    print("Hello {}, you ordered {} more dozens eggs which means your total cost is {}".format(user_name, order_amount, (order_amount * 6.5)))
    print("This means that your overall total comes to {} dozen eggs and ${}".format((name_and_egg_dict[user_name] + order_amount), ((name_and_egg_dict[customer_name] + order_amount) * 6.5))


while True:
    name_entry(name_and_egg_dict)
    if global_loop_variable == "new user":
        first_order(count)
        confirmation(name_and_egg_dict)
        count += 1

    elif global_loop_variable == "name in list":
        returning_order(name_and_egg_dict)

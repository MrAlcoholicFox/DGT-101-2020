######################################################################################################################################
#thoughts and to/dos
##I might need a cost list but probs not
##might need to make some variables global
######################################################################################################################################
name_list = []
egg_amount_list = []
global_loop_variable = None
user_name = None
count = 0
def name_entry(name_list):
    while True:
        user_name = input("Please enter your name (F to finish) ").strip().title()
        break
    if user_name in name_list:
        global global_loop_variable
        global_loop_variable = "name in list"
        return global_loop_variable

    elif user_name == "F":
        global_loop_variable = "Summary"
        return global_loop_variable

    else:
        global_loop_variable = "new user"
        name_list.append(user_name)
        return global_loop_variable

def first_order(name_list, egg_amount_list, count):
    try:
        #add loop thingy
        order_amount = int(input("How many dozen eggs do you want? "))
        print("Hello {}, You ordered {} dozen eggs which means that your total cost is {}".format(name_list[count], order_amount, (order_amount * 6.5)))
    except ValueError:
        print("Please enter a number")

def confirmation(name_list):
    while True:
        confirm = input("Is this correct (yes or no) ").strip().lower()
        if confrim == "yes":
            print("Order Success, Updating Records")
            break
        elif confirm == "no":
            print("Order Aborted")
            break
        else:
            print("please enter yes or no")


while True:
    name_entry(name_list)
    if global_loop_variable == "new user":
        first_order(name_list, egg_amount_list, count)
        confirmation(name_list)
        count += 1

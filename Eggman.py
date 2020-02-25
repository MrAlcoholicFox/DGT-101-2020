#turn ask thing into function maybe
order_list = {}
num = 1
customer_cost = None
while True:
    customer_name = input("Name ('F' to finish): ").strip().title()
    if customer_name == "F":
        break
    elif customer_name in order_list:
        order_amount = int(input("Hello returning customer, how many more eggs would you like? "))
        dozens_of_eggs = order_amount / 12
        total_cost = dozens_of_eggs * 6.5
        print("Welcome back {}, this time you ordered {} eggs which is {:.2f} dozen which means your total order cost is {:.2f}".format(customer_name, order_amount, dozens_of_eggs, total_cost))
        confirmation = input("Is this correct? (yes or no) ").strip().lower()
        if confirmation == "yes":
            print("Order success, updating your record")
            #total_cost is being put in dictionary :/
            order_list[customer_name] += total_cost
    else:
        try:
            order_amount = int(input("How many eggs do you want: "))
            dozens_of_eggs = order_amount / 12
            total_cost = dozens_of_eggs * 6.5
            print("Hello {}, you ordered {} eggs which is {:.2f} dozen which means your total order cost is {:.2f}".format(customer_name, order_amount, dozens_of_eggs, total_cost))
            confirmation = input("Is this correct? (yes or no) ").strip().lower()
            if confirmation == "yes":
                print("Order success, adding to record")
                order_list[customer_name] = order_amount
            elif confirmation == "no":
                print("Order aborted")
            else:
                print("You didn't answer yes or no, please enter your order again")
        except ValueError:
            print("Please enter a Number")    
for name, eggs in order_list.items():
    print("Order {}: {}: {} eggs: ${:.2f}".format(num, name, eggs, total_cost))
    num += 1
#put in summary

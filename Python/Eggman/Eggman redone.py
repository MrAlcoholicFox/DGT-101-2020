####################################################################################################################################
#Thoughts/ to do'
####################################################################################################################################

#global variables I will be using throughout the code to store specific things
order_dict = {}
customer_cost = None
def order_function(order_dict, customer_cost):
    customer_name = ""
    #Makes an infinite loop
    while True:
        while customer_name = "":
        #Asks the user for their name and then checks to see if either; A) the name was f or B) The name had already been used before
        customer_name = input("Name ('F' to finish): ").strip().title()
        if customer_name == "F":
            #Breaks out of the loop so that the summary function can be called and used
            break
        elif customer_name in order_dict:
            #Returning customer code
            while True:
                try:
                    #asks the user how many more dozens eggs they want and gives them an error if they enter something that isn't a number
                    order_amount = int(input("Hello returning customer, how many more dozens eggs would you like? "))
                    total_cost = order_amount * 6.5
                    #prints how many more dozens they ordered and how much more that costs
                    print("Hello {}, you ordered {} more dozens eggs which means your total cost is {}".format(customer_name, order_amount, total_cost))
                    #prints the overall amount of dozens and the total cost
                    print("This means that your overall total comes to {} dozen eggs and ${}".format((order_dict[customer_name] + order_amount), ((order_dict[customer_name] + order_amount) * 6.5)))
                    #asks for the users confirmation for whether the order is correct or not and then branches off depending on the answer
                    while True:
                        confirmation = input("Is this correct? (yes or no) ").strip().lower()
                        if confirmation == "yes":
                            print("Order success, updating your record")
                            order_dict[customer_name] += order_amount
                        elif confirmation == "no":
                            print("Order aborted")
                        else:
                            print("Please enter yes or no")
                except ValueError:
                    print("Please enter a number")
        else:
            while True:
                try:
                    order_amount = int(input("How many dozens eggs do you want "))
                    total_cost = order_amount * 6.5
                    print("Hello {}, you ordered {} dozens eggs which means your total cost is {}".format(customer_name, order_amount, total_cost))
                    while True:
                        confirmation = input("Is this correct? (yes or no) ").strip().lower()
                        if confirmation == "yes":
                            print("Order success, adding to record")
                            order_dict[customer_name] = order_amount
                            break
                        elif confirmation == "no":
                            print("Order aborted")
                            break
                        else:
                            print("Please enter yes or no")
                except ValueError:
                    print("Please Enter A Number!")

#defining the summary function
def summary(order_dict, customer_cost):
    order_num = 1
    for name, dozen in order_dict.items():
        print("Order {} | Name: {} | Dozens: {} | Cost : {}".format(order_num, name, dozen, order_dict[name] * 6.5))
        order_num += 1
                
order_function(order_dict, customer_cost)
summary(order_dict, customer_cost)

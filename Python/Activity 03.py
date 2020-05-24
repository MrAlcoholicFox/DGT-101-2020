MAIN_COURSE_PRICE = 12.50
DESSERT_PRICE = 6
DRINK_PRICE = 3.55

amount_of_mains = int(input("How many Mains are you buying? "))
amount_of_desserts = int(input("How many Desserts are you buying? "))
amount_of_drinks = int(input("How many Drinks are you buying? "))

total_main = MAIN_COURSE_PRICE * amount_of_mains
total_desserts = DESSERT_PRICE * amount_of_desserts
total_drinks = DRINK_PRICE * amount_of_drinks

print("Your total order price for the two of you is: {}".format(total_main + total_desserts + total_drinks))
print("Main course costs: {}".format(total_main))
print("Dessert costs: {}".format(total_desserts))
print("Drinks costs: {}".format(total_drinks))

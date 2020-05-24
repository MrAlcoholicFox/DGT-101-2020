#define the camps banner
def banner():
    print("")
    print("*********************************")
    print("*** Sunshine Holiday Camp™ ***")
    print("*********************************")
    print("")

#define gap
def gap():
    print("")

#call the banner function
banner()

#define name variable and requires for input
childs_name = ""
while len(childs_name) < 2:
    childs_name = input("Please enter name: ").strip()
    if len(childs_name) < 2:
        print("Please enter your name and don't leave it blank")

#define age variable and check to make sure the user is entering a correct value
gap()
while True:
    try:
        childs_age = int(input("Please enter age: "))
        break
    except ValueError:
        print("Please enter a number")

#define the vegetable list
gap()
vegetable_list = ["carrots", "cucumber", "radish", "tomato", "mixed peas and corn", "butter parsnip"]
count = 0
in_list = False
#if age is from age 7 to 10 print the list and get the user to choose their preferred vegetable then print it in a sentence along with other information.
if childs_age <= 10 and childs_age >= 7:
    while count < 6:
        print(vegetable_list[count])
        count += 1
    while in_list == False:
        vege_choice = input("What vegetable do you want: ")
        if vege_choice in vegetable_list:
            in_list = True
    print("{} is {} years old and their vegetable choice is {}".format(childs_name, childs_age, vege_choice))

#if the user is older than 10 and younger than 12 than tell them they don't need to choose a vegetable
elif childs_age > 10 and childs_age <= 12:
    print("Since {} is {} years old they don't need to choose vegetable".format(childs_name, childs_age))

#If the user does not fit the age requirements for Sunshine Holiday Camp™ then deny them :3
else:
    print("Sorry but {} cannot attend the Sunshine Holiday Camp™ because they don't fit the age requirements for Sunshine Holiday Camp™".format(childs_name))
#call banner function again
banner()

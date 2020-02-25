children_dict = {}
#define the banner for the camp
def banner():
    print("*******************************")
    print("*** Sunshine Holiday Camp ***")
    print("*******************************")

#call the banner function
banner()

#collect the names, ages and if required vegetable
while True:
    try:
        childs_name = input("Name (F to finish): ").strip().title()
        if childs_name == "F":
            break
        childs_age = int(input("Age: "))
        if childs_age >= 7 and childs_age <= 12:
            print("{}, Welcome to Camp".format(childs_name))
            children_dict[childs_name] = childs_age
        el
    except ValueError:
        print("Please enter a valid age")


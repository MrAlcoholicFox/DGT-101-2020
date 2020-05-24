name = input("Please enter name: ")
user_height = int(input("Please enter your height: "))

if user_height == 175:
    print("Congratulations, {} you are as tall as Justin Bieber.".format(name))

elif user_height != 175:
    print("Sorry, {} but you arent as tall as Justin Bieber.".format(name))

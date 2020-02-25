PIN = 1234
pin_trys = 3
pin_attempt = None
while pin_attempt != PIN and pin_trys > 0:
    try:
        pin_attempt = int(input("Please enter your pin: "))
        if pin_attempt == PIN:
            break
        print("Sorry that is incorrect please try again ")
        pin_trys -= 1
    except ValueError:
        print("Please enter a number ")
        pin_trys -= 1
if pin_trys == 0:
    print("You're all out of attempts, please try again later")

elif pin_attempt == PIN:
    print("Welcome to your computer *makes windows 95 sounds*")

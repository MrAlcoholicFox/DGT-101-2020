name = input("What is your name? ")
planet_of_origin = input("What planet are you from? ")
planet_of_origin.lower()
if planet_of_origin == "earth":
    print("Hello {} My Earthling Friend".format(name))
else:
    print("Hello {} my Friend From the Universe".format(name))

name = input("What is your name? ")
age = int(input("What is your age? "))
year_group = int(input("What year group do you belong to in kc e.g 11: "))
birthday = input("Have you had your birthday yet? ")
birthday.lower()
birth_year = None
if birthday == "yes":
    birth_year = 2020 - age
elif birthday == "no":
    birth_year = 2019 - age
print("Hello, {}. you were born in {}".format(name, birth_year))
print("you have {} years left at kc".format(13 - year_group))

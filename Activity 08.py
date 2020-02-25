Name = input("Please enter your name: ")
while True:
    try:
        points_at_merit = int(input("How many Merit points did you get for this course "))
        points_at_excellence = int(input("How many Excellence points did you get for this course "))
        break
    except ValueError:
        print("Please enter a numerical number")
points_overall = points_at_merit + points_at_excellence

if points_overall >= 14:
    print("Congratulations, {} you have an endorsement")
else: 

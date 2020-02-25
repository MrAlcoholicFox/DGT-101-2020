import random

#Create a list of responses
responses = ["Yes", "No", "Maybe", "Outlook Doubtful", "It is impossible to say", "Try again later", "Are you gonna finish that Croissant", "Perhaps"]

#Ask the user for their name and store it, welcome the user
name = input("What is your name?").title()
print("Hi {}, this Magic 8 Ball can answer all of your burning questions".format(name))

#Use a loop to let the user ask their questions
repeat = True
while repeat == True:
  question = input("Please ask a yes or no question or type 'done' to quit:").strip().lower()
  
  if question == "done":
    print("All the best for the future, {}. Goodbye!".format(name))
    repeat = False
  else:
    random.shuffle(responses)
    print(responses[0])
    

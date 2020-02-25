# Print out the menu so the user knows what options there are and get user's choice
def menu():
    
  mode = input("""Choose a mode by entering the number:
  1: Add a task
  2: View list
  3: Exit
  """).strip()

  return mode

# Function that allows user to add a task to their to do list
def add_tasks():
  while True:
    new_task = input("Enter the task to add or type 'end' to return to menu: ").strip().lower()
    if new_task == "end":
      break
    else:
      todo_list.append(new_task)

# Function that shows current tasks in the To Do List
def view_list():
  if len(todo_list) > 0:
    for task in todo_list:
      print("- {}".format(task))
  else:
    print("You have no tasks yet!")

# Create an empty list to store the tasks
todo_list = []

# Run the main program in a loop.
while True:
  chosen_option = menu()

  if chosen_option == "1":
    add_tasks() 
  elif chosen_option == "2":
    print("Here is your To Do List:")
    view_list()
  elif chosen_option == "3":
    break
  else:
    print("That wasn't an option, please try again")
print("Goodbye")

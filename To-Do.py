# Initialize an empty list to store tasks
tasks = []

# Function to add a new task to the list
def add_task():
    # Ask the user to enter a task
    task = input('Please enter your task: ')
    # Append the task to the tasks list
    tasks.append(task)
    # Print a success message
    print(f'The task "{task}" has been added successfully! 😊')

# Function to display all tasks in the list
def all_tasks():
    # Check if there are tasks in the list
    if tasks:
        # Print all tasks with their indexes
        print('All Tasks: ')
        for index, task in enumerate(tasks):
            print(f'Task {index}. {task}')
    else:
        # Print a message if no tasks are found
        print('No tasks found! 😟')

# Function to edit an existing task in the list
def edit_task():
    # Display all tasks to the user
    print('Here is all the list of your tasks: ')
    all_tasks()
    try:
        # Ask the user to enter the index of the task to edit
        to_be_edited_task = int(input('Please enter the index number of the task to edit: '))
        # Check if the provided index is valid
        if 0 <= to_be_edited_task < len(tasks):
            # Prompt the user to enter the new task details
            new_task = input('Please Enter the new task details: ')
            # Update the task in the list
            tasks[to_be_edited_task] = new_task
            # Print a success message
            print(f'The Task {to_be_edited_task} has been updated successfully 😊')
        else:
            # Print an error message if the index is invalid
            print('The index number you provided is invalid! 😟')
    except ValueError:
        # Handle the case when the user enters an invalid input
        print('Invalid input. Please enter a valid index number.')

# Function to delete a task from the list
def delete_task():
    # Display all tasks to the user
    print('Here is all the list of your tasks: ')
    all_tasks()
    try:
        # Prompt the user to enter the index of the task to delete
        to_be_deleted_task = int(input('Please enter the index number which is to be deleted: '))
        # Check if the provided index is valid
        if 0 <= to_be_deleted_task < len(tasks):
            # Remove the task from the list
            tasks.pop(to_be_deleted_task)
            # Print a success message
            print(f'The Task {to_be_deleted_task} has been deleted successfully 😊')
        else:
            # Print an error message if the index is invalid
            print('The index number you provided is invalid! 😟')
    except ValueError:
        # Handle the case where the user enters an invalid input
        print('Invalid input. Please enter a valid index number.')

# Main program
        
if __name__ =="__main__": # Runs within the module and cannot be run when imported
    # Print a welcome message
    print('Welcome to the To-Do-List App!')

    # Main loop for user interaction
    while True:
        # Display menu options to the user
        print('\nChoose the Letter Accordingly!!!')
        print('**********************')
        print('A. Add your Task')
        print('L. List your Task')
        print('E. Edit your Task')
        print('D. Delete your Task')
        print('Q. Quit')

        # Prompt the user to enter their choice
        users_input = input('Please enter your choice: ')

        # Process user input based on the chosen option
        if (users_input=='A'):
            add_task()
        elif (users_input=='L'):
            all_tasks()
        elif(users_input=='E'):
            edit_task()
        elif(users_input=='D'):
            delete_task()
        elif(users_input=='Q'):
            # Exit the program if the user chooses to quit
            break
        else:
            # Print an error message for invalid input
            print('The Input choice is invalid. Please Try Again later! 😟')

    # Print a farewell message when the program exits
    print('Thank you for using the App!!! 🙋‍♂️🙋‍♂️🙋‍♂️')

#used OOP to make a Task class
class Task:
    def __init__(self, name):
        self.name = name
        #made tasks in a list
        self.tasks = []
#main menu function with exception handling errors
    def main_menu_choice(self):
        while True:
            try:
                print("===Ziad nader To-do list ===")
                x = int(input("Welcome to the main menu! Please choose your option:\n"
                              "1 - Add tasks\n"
                              "2 - Show tasks\n"
                              "3 - Remove tasks\n"
                              "4 - Mark tasks as done\n"
                              "5 - Exit\n"))
                return x
            except ValueError:
                print("Please choose a valid input.")
#the decision making function that asks the user about his decision
    def decision_making(self, x):
        if x == 1:
            try:
                z = int(input("Enter the number of tasks you wish to add: "))
                for i in range(z):
                    task = input("Write the task you wish to add: ")
                    self.tasks.append(task)
                    print(f"The task '{task}' was added successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            self.main_menu()

        elif x == 2:
            print("Your tasks are:")
            if not self.tasks:
                print("No tasks to show.")
            else:
                for i, task in enumerate(self.tasks, 1):
                    print(f"{i}. {task}")
            self.main_menu()

        elif x == 3:
            try:
                print("Choose the task you want to remove:")
                for i, task in enumerate(self.tasks, 1):
                    print(f"{i}. {task}")
                task_num = int(input("Enter the number of the task you want to remove: "))
                if 0 < task_num <= len(self.tasks):
                    removed_task = self.tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' was removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            self.main_menu()

        elif x == 4:
            try:
                print("Choose the task you wish to mark as done:")
                for i, task in enumerate(self.tasks, 1):
                    print(f"{i}. {task}")
                task_num = int(input("Enter the number of the task you wish to mark as done: "))
                if 0 < task_num <= len(self.tasks):
                    self.tasks[task_num - 1] += " [Done]"
                    print(f"Task '{self.tasks[task_num - 1]}' was marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            self.main_menu()

        elif x == 5:
            print("Thanks for using my simple to-do list program!")
            rasie SystemExit
        
        elif x<=0 or x>5:
            print("please choose a number for your option between 1-5")

    def main_menu(self):
        while True:
            choice = self.main_menu_choice()
            
            self.decision_making(choice)
#called the main function
task1 = Task("ziad")
task1.main_menu()

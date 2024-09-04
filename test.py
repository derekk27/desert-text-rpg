import csv


list = {"do dishes": ["home", "None", True], "Gym": ["None", "None", False], "walk dog": ["home", "None", True]}

category_list = ["home", "work", "school"]

enumlist = enumerate(category_list, 1)

todolist = []

lista = ["a","b","c", "d","e"]
listb = ["x","y","z"]


listb.append(lista.pop(2))

print(lista, listb)
"""
class Task:
    
    def __init__(self, name:str, category:str, due, prio: bool):
        self.name = name
        self.category = category
        self.due = due
        self.isCompleted = False
        self.prio = False
    

    def setCategory(self, category):
        self.category = input("type the category of this task")
    
    def setDue(self, due):
        self.due = input("Pick when this task should be done by")
    
    def editTask(self, name):
        self.name = input("Type in the new task: ")
    
    def setPrio(self, prio):
        self.prio = True

def view_tasks(self):
        print("Current list of categories:")
        for index, task in enumerate(category_list, start=1):
            print(f"{index}. {task}")



def showtodo():
    with open(todolist, 'w', newline='') as csvfile:
        fieldnames = ['name', 'category', 'due', 'isCompleted', 'prio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in ToDoList:
            writer.writerow({
                'name': task.name,
                'category': task.category,
                'due': task.due,
                'isCompleted': task.isCompleted,
                'prio': task.prio})
            

def loadAllTask():
    with open('todolist.csv', newline='') as csvfile:
        todocsv = csv.reader(csvfile, delimiter=",")
        next(todocsv)
        PrioList = []
        nonPrioList = []
        
        print("Priority tasks: \n")
        for index, row in enumerate(todocsv, start=1):
            if row[-1] == True:
                print(f"{index}. {row[0]}")
                PrioList.append(row[0]) #if prio == True, print them out and append to the PrioList.
            else:
                nonPrioList.append(row[0])
        print("All other tasks: ")
        for index, task in enumerate(nonPrioList, start=1):
            print(f"{index}. {task}")

            


def addTask():
    
    name = input("Enter task name: ")
    category = input(f"Enter task category: ")
    due = input("Enter task due date: ")
    prio = input("Is this task priority? (yes/no): ").lower() == "yes"
    newTask = Task(name, category, due, prio)

    with open('todolist.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'category', 'due', 'isCompleted', 'prio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # Check if file is empty
            writer.writeheader()

        writer.writerow({
            'name': newTask.name,
            'category': newTask.category,
            'due': newTask.due,
            'isCompleted': newTask.isCompleted,
            'prio': newTask.prio
        })


def clear():
    pass

print(len(category_list))
"""


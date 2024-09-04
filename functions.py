from datetime import datetime
import csv
import fileinput
import os

class Task:
    
    def __init__(self, name, category, due, isCompleted, prio):
        self.name = name
        self.category = category
        self.due = due
        self.isCompleted = isCompleted
        self.prio = prio
    
    def __repr__(self):
        return self.name

    def setCategory(self, category):
        self.category = input("type the category of this task")
    
    def setDue(self, due):
        self.due = datetime.strptime(input("Enter due date (YYYY-MM-DD)", "%Y-%m-%d"))
    
    def editTask(self, name):
        self.name = input("Type in the new task: ")
    
    def setPrio(self, prio):
        self.prio = True


PrioList = []
nonPrioList = []
completedList = []

categoryList = ["home", "work", "school"]
todolist = []

def loadAllTask():
    with open('todolist.csv', newline='') as csvfile:
        todocsv = csv.reader(csvfile, delimiter=",")
        next(todocsv)

        for row in todocsv:
            if row[-2] == "True":
                completedList.append(Task(row[0], row[1], row[2], row[3], row[4]))
            elif row[-1] == "True":
                PrioList.append(Task(row[0], row[1], row[2], row[3], row[4])) #if prio == True, print them out and append to the PrioList.
            else:
                nonPrioList.append(Task(row[0], row[1], row[2], row[3], row[4])) #all the nonprio tasks gets added to nonPrioList

def main():
    running = True
    
    
    if PrioList == [] and nonPrioList == [] and completedList ==[]:
        loadAllTask()

    while running == True:

        userinput = input("Choose an action: (type a number) \n\
1. Add task \n\
2. Complete a task \n\
3. Delete a task \n\
4. Show task list \n\
5. Categories \n\
6. Quit \n")

        match userinput:
            case "1":
                addTask()
            case "2":
                completeTask()
            case "3":
                deleteTask()
            case "4":
                ShowList()
            case "5":
                userinput = input("Categories menu. Choose an action: \n1. Add a category \n2. Delete a category\n3. Show list of categories \n4. Back to main menu \n")
                match userinput:
                    case "1":
                        addCategory()
                    case "2":
                        deleteCategory()
                    case "3":
                        showCategoryList()
                    case "4":
                        main()
            case "6":
                print("See you later!")
                
                running = False
                break
        

def ShowList():
    print("PRIORITY TASKS:")
    for index, task in enumerate(PrioList, start = 1):
            print(f"{index}. {task}")
    print(f"Remaining priority tasks: {len(PrioList)} \n")
    print("All other tasks: ")
    for index, task in enumerate(nonPrioList, start=len(PrioList)+1):
        print(f"{index}. {task}")
    print(f"Total number of tasks: {len(PrioList) + len(nonPrioList)}")
    print(f"Completed tasks: {len(completedList)}")


def addTask():
    
    name = input("Enter task name: ")
    category = input("Enter task category: ")
    due = datetime.strptime(input("Enter due date (YYYY-MM-DD)"), "%Y-%m-%d")
    prio = input("Is this task priority? (y/n): ").lower() == "y"
    isCompleted = False
    newTask = Task(name, category, due, isCompleted, prio)
    
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

def deleteTask():
    ShowList()
    numbertodelete = int(input("Type the number of task to delete")) -1
    if numbertodelete > len(PrioList) or len(PrioList) == 0:
        #if the task number is greater than prioritylist length, subtract the length of prio list and find it from the nonpriolist
        numbertodelete -= len(PrioList)
        nonPrioList.pop(numbertodelete)
        with open("todolist.csv", 'w', newline='') as csvfile:
            fieldnames = ['name', 'category', 'due', 'isCompleted', 'prio']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in PrioList:
                writer.writerow({
                    'name': task.name,
                    'category': task.category,
                    'due': task.due,
                    'isCompleted': task.isCompleted,
                    'prio': task.prio
                })
            for task in nonPrioList:
                writer.writerow({
                    'name': task.name,
                    'category': task.category,
                    'due': task.due,
                    'isCompleted': task.isCompleted,
                    'prio': task.prio
                })
    else:
        PrioList.pop(numbertodelete)
        with open("todolist.csv", 'w', newline='') as csvfile:
            fieldnames = ['name', 'category', 'due', 'isCompleted', 'prio']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in PrioList:
                writer.writerow({
                    'name': task.name,
                    'category': task.category,
                    'due': task.due,
                    'isCompleted': task.isCompleted,
                    'prio': task.prio
                })
            for task in nonPrioList:
                writer.writerow({
                    'name': task.name,
                    'category': task.category,
                    'due': task.due,
                    'isCompleted': task.isCompleted,
                    'prio': task.prio
                })
    print("Task deleted successfully")


def addCategory():
    print("Current list of categories:")
    for index, task in enumerate(categoryList, start=1):
        print(f"{index}. {task}")
    answer = input("type a category to add: ").strip()
    if answer in categoryList:
        print("category already exists!")
    else:
        categoryList.append(answer)
        print(f"{answer} has been added to the list of categories")

def deleteCategory():
    print("Current list of categories:")
    for index, task in enumerate(categoryList, start=1):
        print(f"{index}. {task}")
    answer = input("type a category to delete: ").strip()
    if answer in categoryList:
        if input(f"Deleting {answer} from the category list. Are you sure? (y/n) ") == "y":
            categoryList.remove(answer)
            print("Successfully removed!")

    else:
        print(f"{answer} category does not exist!")

def showCategoryList():
    print("Current list of categories:")
    for index, task in enumerate(categoryList, start=1):
        print(f"{index}. {task}")

def completeTask():
    ShowList()
    tasknumber = int(input("Select which task has been completed: ")) -1
    if tasknumber > len(PrioList) or len(PrioList) == 0:
        #if the task number is greater than prioritylist length, subtract the length of prio list and find it from the nonpriolist
        tasknumber -= len(PrioList)
        for line in fileinput.input('todolist.csv', inplace = True):
            # print("line: ", line)
            csvtask = line.strip().split(',') #turns the line into array
            # print("csvtask: ", csvtask)
            if nonPrioList[tasknumber].name == csvtask[0]:
                # print("inside nonprio list task if")
                csvtask[3] = "True" # turns isComplete to True in palce
                completedList.append(nonPrioList[tasknumber].pop(tasknumber))
            print(','.join(csvtask)) #rejoins the array into csv format (line)
    else:
        for line in fileinput.input('todolist.csv', inplace = True):
            csvtask = line.strip().split(',')
            if PrioList[tasknumber].name == csvtask[0]:
                line[2] = True
                completedList.append(PrioList[tasknumber].pop(tasknumber))
            print(','.join(csvtask)) #rejoins the array into csv format (line)




def showCompleted(): #shows completed tasks
    pass
def showCategory(): #shows tasks under a specific category
    pass
def pastDD(): #highlights tasks that are past due date
    pass

main()
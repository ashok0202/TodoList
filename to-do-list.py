tasks=[]

def add_task(task):
    """
    Add a new Task to the To-Do-List
    """
    tasks.append(task)
    print("Added task :", task)

def remove_task(task):
    """
    Remove a Task From To-Do-List
    """
    if task in tasks:
        tasks.remove(task)
        print("Remove Task :",task)
    else:
        print(f"{task} Not Found")

def view_task():
    """
    View all Tasks in List
    """
    print("To-Do-List")
    if not tasks:
        print("No tasks in the list")
    else:
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")

#main Program loop 
while True:
    print("\n What you want to do")
    print("1. Add a task")
    print("2. Remove a Task")
    print("3. View all Task")
    print("4. Exit")

    choice=input("Enter Choice: ")
    if choice=="1":
        task=input("Enter New task ")
        add_task(task)

    elif choice=="2":
        task=input("Enter task To remove: ") 
        remove_task(task)

    elif choice=="3":
        view_task()

    elif choice=="4":
        print("Exiting ")
        break

    else:
        print("Invalid Choice !")
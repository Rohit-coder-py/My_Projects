import datetime
print('''--- My To-Do List App ---

1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit''')
c1m='''
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit'''

task={

}
def addtask():
    a1 = input("Which task you want to add:")
    task.update({a1:"Pending⌚"})
    print("Task added Successfully☑️")
    
def viewtask():
    b1=input("Press Enter if you want to view all task:")
    print("--Your Tasks--")
        
        
def markascomplete():
    pqw=datetime.datetime.now()
    c1=input("Enter task name to mark complete:")
    if c1 in task:
        print(f"Task {c1} marked as completed suceesfully☑️")
        task[c1]=f"☑Completed on{pqw}"
    else:
        print("This task is not found in your To-Do List.Please fill accuarate name of the task")
        
        
def deletetask():
    d1=input("Which task you want to delete:")
    if d1 in task:
        print(f"🗑 Task {d1} deleted successfully!")
        task.pop(f"{d1}")
    else:
        print("This task is not found in your list")
def exit():
    print("👋 Exiting... Have a productive day!")
    
    
input("Press Enter to Begin:")
while True:
    choose=int(input("Enter your choice:"))
    if choose==1:
        addtask()
        
    elif choose==2:
        viewtask()
        for task,status in task.items():
            print(f"⭕{task} - {status}")
    elif choose==3:
        markascomplete()
    elif choose==4:
        deletetask()
    elif choose==5:
        exit()
        break
    else:
        print("Invalid Input Recived . Please fill from 1 to 5")
    

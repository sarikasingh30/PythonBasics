# Todo App

tasks=[]
while True:
    x=input("............\n MENU: \n 1. Add Tasks \n 2. View Tasks \n 3. Edit task \n 4. Delete task \n 5. Quit \n Entr your Choice: ")

    if(x=="1"):
        ans=input("Enter the Task: ")
        bal={}
        bal["title"]=ans
        bal["status"]=False
        tasks.append(bal)
    elif(x=='2'):
        print("Tasks: ")
        for index,task in enumerate(tasks,start=1):
            print(f"{index} {task}")
    elif(x=='3'):
        for index,task in enumerate(tasks,start=1):
            print(f"{index} {task}")
        val=int(input("Select the index of the task you want to Edit: "))
        if(1<=val<=len(tasks)):
            valS=input("Choose between title and status:")
            if(valS=='title'):
                    print("Original Value:", {tasks[val-1]["title"]})
                    nval=input("Enter New Value: ")
                    tasks[val-1]["title"]=nval
                
            elif(valS=='status'):
                    print("Original Value:", {tasks[val-1]["status"]})
                    tasks[val-1]["status"]= not(tasks[val-1]["status"])
        else:
            print("Invalid Index.....")

    elif(x=='4'):
        for index,task in enumerate(tasks,start=1):
            print(f"{index} {task}")
        val=int(input("Select the index of the task you want to Delete: "))
        if(1<=val<=len(tasks)):
            deletedTask=tasks.pop(val-1)
            print(f"Deleted Task: {deletedTask}")
        else:
            print("Invalid Index.....")
    elif(x=='5'):
        break;
    else:
        print("Invalid Choice...")
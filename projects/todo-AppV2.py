# Todo App

tasks=[]
while True:
    x=input("............\n MENU: \n 1. Add Tasks \n 2. View Tasks \n 3. Search task \n 4. Edit task \n 5. Delete task \n 6. Quit \n Entr your Choice: ")

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
    
    elif(x=="3"):
         # Searching Functionality 
        ans=input("Choose between title and status: ")
        if(ans=="status"):
            statusValforSearch=bool(input("Select the Status: "))
            searchAns=[]
            for i in tasks:
                if(i["status"]==statusValforSearch):
                    searchAns.append(i)
            print(searchAns)
        elif(ans=="title"):
            titleValforSearch=input("Select the Title: ")
            searchTans=[]
            for j in tasks:
                if(j["title"]==titleValforSearch):
                    searchTans.append(j)
            print(searchTans)
            
        else:
            print("Invalid Choice...........")


    elif(x=='4'):
        for index,task in enumerate(tasks,start=1):
            print(f"{index} {task}")
        val=int(input("Select the index of the task you want to Edit: "))
        if(1<=val<=len(tasks)):
            valS=input("Choose between title and status: ")
            if(valS=='title'):
                    print("Original Value:", {tasks[val-1]["title"]})
                    nval=input("Enter New Value: ")
                    tasks[val-1]["title"]=nval
                
            elif(valS=='status'):
                    print("Original Value:", {tasks[val-1]["status"]})
                    tasks[val-1]["status"]= not(tasks[val-1]["status"])
        else:
            print("Invalid Index.....")

    elif(x=='5'):
        for index,task in enumerate(tasks,start=1):
            print(f"{index} {task}")
        val=int(input("Select the index of the task you want to Delete: "))
        if(1<=val<=len(tasks)):
            deletedTask=tasks.pop(val-1)
            print(f"Deleted Task: {deletedTask}")
        else:
            print("Invalid Index.....")
    elif(x=='6'):
        break;
    else:
        print("Invalid Choice...")
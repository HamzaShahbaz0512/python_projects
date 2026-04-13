

class Task:
    def __init__(self,name,depend_on=None,Difficulty=None,status="pending"):
        self.name=name
        self.depend_on=depend_on
        self.difficulty=Difficulty
        self.status=status
tasks={}
    
def add_task(name,depend_on=None,Difficulty=None,status="pending"):
    if name in tasks:
        print("Task already exists")
        return
    if(depend_on and depend_on not in tasks):
        print("Dependent task does not exist")
        return
    tasks[name]=Task(name,depend_on,Difficulty)
    print(f"Task {name} added")
        
#Print Task Data
def print_data():
    if(tasks):
        for task in tasks.values():
            print(f"task name:{task.name}, Dependent on: {task.depend_on},Difficulty={task.difficulty},Status={task.status}")

#Delete task function
def delete_task(name):
    
    if(name not in tasks):
        print("Task not found")
        return
    print("Task exists")
    del tasks[name]
   
   #update Task
def Update_task(name,depend_on,difficulty,status):
    if(name not in tasks):
        print("Task not found")
        return
    
    if(status=="completed"):
        for t in tasks.values():
            if t.status!="completed":
                print(f"Cannot mark {name} as completed because dependent task {t.name} is not completed")
                return
    
    if name:
        task=tasks[name]
    if depend_on:
        task.depend_on=depend_on
    if difficulty:
        task.difficulty=difficulty
    if status:
        task.status=status
    print(f"Task {name} updated")
    
def get_dependent_tasks(name):
    for t in tasks.values():
        if t.depend_on==name:
            print(f"Task {t.name} is dependent on {name}")
    
def get_independent_tasks():
    for t in tasks.values():
        if t.depend_on==None or t.depend_on =="":
            print(f"{t.name} is not dependent on any task")
            
#Get details about specific task

def get_task_details(name):
    if(name not in tasks):
        print("Task not found")
        return
    task=tasks[name]
    print(f"task name:{task.name}, Dependent on: {task.depend_on}, Difficulty={task.difficulty},Status={task.status}")



#testing it


if __name__ == "__main__":

    for i in range(40):
        action=input("Enter action (add, delete, update, get details, print data, get dependent tasks, get independent tasks): ")
        
        if action=="add":   
            print("\n")
            input_name=input("Enter task name: ")
            input_depend_on=input("Enter dependent task name (or press enter if none): ")
            input_difficulty=input("Enter task difficulty (or press enter if none): ")
            add_task(input_name, input_depend_on, input_difficulty)
        
        elif action=="update":
            print("\n")
            input_name=input("Enter task name to update: ")
            input_depend_on=input("Enter new dependent task name (or press enter if none): ")
            input_difficulty=input("Enter new task difficulty (or press enter if none): ")
            input_status=input("Enter new task status (pending/completed): ")
            Update_task(input_name, input_depend_on, input_difficulty,input_status)
        
        elif action=="delete":
            print("\n")
            input_delete=input("Enter task name to delete: ")
            delete_task(input_delete)
        
        elif action=="get details":
            print("\n")
            input_name=input("Enter task name to get details: ")
            get_task_details(input_name)
            
        elif action=="print data":
            print_data()
        
        elif action=="get dependent tasks":
            print("\n")
            input_name=input("Enter task name to get dependent tasks: ")
            get_dependent_tasks(input_name)    
  
        elif action=="get independent tasks":
            print("\n")
            get_independent_tasks()
    input_delete=input("Enter task name to delete: ")
    delete_task(input_delete)
    print_data()
    
    
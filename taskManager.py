

class Task:
    def __init__(self,name,depend_on=None,Difficulty=None):
        self.name=name
        self.depend_on=depend_on
        self.difficulty=Difficulty
        self.completed=False
tasks={}
    
def add_task(name,depend_on=None,Difficulty=None):
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
    for task in tasks.values():
        print(f"task name:{task.name}, Dependent on: {task.depend_on},Difficulty={task.difficulty}")

#Delete task function
def delete_task(name):
    
    if(name not in tasks):
        print("Task not found")
        return
    print("Task exists")
    del tasks[name]
        
        
        
        
#testing it

count=int(input("How many times do you want to add tasks? "))

for i in range(count):
    input_name=input("Enter task name: ")
    input_depend_on=input("Enter dependent task name (or press enter if none): ")
    input_difficulty=input("Enter task difficulty (or press enter if none): ")
    print("\n")
    add_task(input_name, input_depend_on, input_difficulty)

print("\n")
print_data()

input_delete=input("Enter task name to delete: ")
delete_task(input_delete)

print("\n")

print("After Deleting the task:")
print_data()
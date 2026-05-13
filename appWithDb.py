from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
db=SQLAlchemy(app)

class Task(db.Model):
    id:Mapped[int]=db.Column(db.Integer,primary_key=True)
    name:Mapped[str]=db.Column(db.String(100),nullable=False)
    depend_on:Mapped[str]=db.Column(db.String(100),nullable=True)
    difficulty:Mapped[str]=db.Column(db.String(50),nullable=True)
    status:Mapped[str]=db.Column(db.String(20),nullable=False,default="pending")


with app.app_context():
    db.create_all()
    
print("Database created successfully")


#create task
@app.route('/tasks',methods=["POST"])
def add_tasks():
    data=request.get_json()
    id=data.get('id')
    name=data.get("name")
    depend_on=data.get("depend_on")
    difficulty=data.get("difficulty")
    status=data.get("status")

    if(Task.query.get(id)):
        return jsonify({'error':'Task already exists'}),400
    
    task=Task(id=id,name=name,depend_on=depend_on,difficulty=difficulty,status=status)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': f'Task {id} added'}),201

#Get all tasks
@app.route('/tasks',methods=['GET'])
def get_tasks():
    tasks=Task.query.all()
    print("task is : ",tasks)
    result={
        task.id: {
            "id": task.id,
            "name": task.name,
            "depend_on": task.depend_on,
            "difficulty": task.difficulty,
            "status": task.status
        }
        for task in tasks
    }
    return jsonify(result)

#Get a specific Item
@app.route('/tasks/<id>',methods=['GET'])
def getTask(id):
    tasks=Task.query.get(id)
    if not tasks:
        return jsonify({'error':'Task does not exist'}),404
    result={
        "id":tasks.id,
        "name":tasks.name,
        "depend_on":tasks.depend_on,
        "difficulty":tasks.difficulty,
        "status":tasks.status
    }
    return jsonify(result)
    
#update a specific
@app.route('/tasks/<id>',methods=['PUT'])
def update_task(id):
    data=request.get_json()
    task=Task.query.get(id)
    if not task:
        return jsonify({"error": "Task does not exist"}), 404
    if data.get('name'):
        task.name=data.get("name")
    if data.get('depend_on'):
        task.depend_on=data.get("depend_on")
    if data.get('difficulty'):
        task.difficulty=data.get("difficulty")
    if data.get('status'):
        task.status=data.get("status")
    db.session.commit()
    return jsonify({{"message":f"task {id} updated"}}),200

#Delete a specific task
@app.route('/tasks/<id>',methods=['DELETE'])
def delete_task(id):
    task=Task.query.get(id)
    if not task:
        return jsonify({"error": "Task does not exist"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": f"Task {id} deleted"}), 200

if(__name__=='__main__'):
    app.run(debug=True)

'''
class Task:
    def __init__(self,id,name,depend_on=None,Difficulty=None,status="pending"):
        self.id=id
        self.name=name
        self.depend_on=depend_on
        self.difficulty=Difficulty
        self.status=status
        
tasks = {}
'''
#Get all items
'''

@app.route('/tasks',methods=['GET'])
def get_tasks():
    result = {}
    for id, task in tasks.items():
        result[id] = {
            "id":task.id,
            "name": task.name,
            "depend_on": task.depend_on,
            "difficulty": task.difficulty,
            "status": task.status
        }
    return jsonify(result)

#Create an item

@app.route('/tasks',methods=['POST'])
def add_Task():
    data = request.get_json()
    id=data.get('id')
    name=data.get('name')
    if id in tasks:
        return jsonify({'error':'Task already exists'}) ,400
    tasks[id] = Task(id,name)
    tasks[id].depend_on=data.get("depend_on")
    tasks[id].difficulty=data.get("difficulty")
    tasks[id].status=data.get("status")
    return jsonify({'message': f'Task {id} added'}), 201

#Update a specific item
@app.route('/tasks/<id>',methods=['PUT'])

def update_task(id):
    data=request.get_json()
    if id not in tasks:
        return jsonify({'error':'Task not found'}), 404
    
    if data.get('name'):
        tasks[id].name = data.get('name')
    if data.get('depend_on'):
        tasks[id].depend_on = data.get('depend_on')
    if data.get('difficulty'):
        tasks[id].difficulty = data.get('difficulty')
    if data.get('status'):
        tasks[id].status = data.get('status')
    return jsonify({'message': f'Task {id} updated'})

#Get a specific item. Added some lines to the comment
@app.route('/tasks/<id>',methods=['GET'])

def get_item(id):
    if id not in tasks:
        return jsonify({'error':'Task not found'}), 404
    data1={
        "id": tasks[id].id,
        "name": tasks[id].name,
        "depend_on": tasks[id].depend_on,
        "difficulty": tasks[id].difficulty,
        "status": tasks[id].status
    }
    return jsonify(data1)
@app.route('/tasks/<id>',methods=['DELETE'])

def delete_task(id):
    if id not in tasks:
        return jsonify({'error':'Task not found'}), 404
    del tasks[id]
    return jsonify({'message': f'Task {id} deleted'})

if(__name__=='__main__'):
    app.run(debug=True)
    '''

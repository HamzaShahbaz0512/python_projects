from flask import Flask,jsonify,request

app = Flask(__name__)

class Task:
    def __init__(self,id,name,depend_on=None,Difficulty=None,status="pending"):
        self.id=id
        self.name=name
        self.depend_on=depend_on
        self.difficulty=Difficulty
        self.status=status
        
tasks = {}

#Get all items

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
    

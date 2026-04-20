from flask import Flask,jsonify,request

app = Flask(__name__)

class Task:
    def __init__(self,name,depend_on=None,Difficulty=None,status="pending"):
        self.name=name
        self.depend_on=depend_on
        self.difficulty=Difficulty
        self.status=status
        
tasks = {}

@app.route('/tasks',methods=['GET'])
def get_tasks():
    result = {}
    for name, task in tasks.items():
        result[name] = {
            "name": task.name,
            "depend_on": task.depend_on,
            "difficulty": task.difficulty,
            "status": task.status
        }
    return jsonify(result)

@app.route('/tasks',methods=['POST'])
def add_Task():
    data = request.get_json()
    name=data.get('name')
    if name in tasks:
        return jsonify({'error':'Task already exists'}) ,400
    tasks[name] = Task(name)
    return jsonify({'message': f'Task {name} added'}), 201


if(__name__=='__main__'):
    app.run(debug=True)
    

from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///pipt.db"
db=SQLAlchemy(app)


class User(db.Model):
    id:Mapped[int]=db.Column(db.Integer,primary_key=True)
    name:Mapped[str]=db.Column(db.String(100),nullable=False)
    password:Mapped[str]=db.Column(db.String(100),nullable=False)
    
class Task(db.Model):
    id:Mapped[int]=db.Column(db.Integer,primary_key=True)
    name:Mapped[str]=db.Column(db.String(100),nullable=False)
    depend_on:Mapped[str]=db.Column(db.String(100),nullable=True)
    difficulty:Mapped[str]=db.Column(db.String(50),nullable=True)
    status:Mapped[str]=db.Column(db.String(20),nullable=False,default="pending")


with app.app_context():
    db.create_all()
app.config['JWT_SECRET_KEY']='1A2B3C4D'
JWT = JWTManager(app)

print("Database created successfully")

#Create User
@app.route('/register',methods=["POST"])
def add_user():
    data=request.get_json()
    id=data.get('id')
    name=data.get("name")
    password=data.get("password")
    
    if(User.query.filter_by(name=name).first()):
        return jsonify({'error':'User with this name already exists'}),400

    hashed_password=generate_password_hash(password)
    

    new_user=User(id=id,name=name,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': f'User registered {id} added'}),201

#Login User
@app.route('/login',methods=["POST"])
def login_user():
    data=request.get_json()
    name=data.get("name")
    password=data.get("password")

    user=User.query.filter_by(name=name).first()
    if not name or not check_password_hash(user.password,password):
        return jsonify({"error":"Invalid user credentials"}),401
    token = create_access_token(identity=str(name))
    return jsonify({"message": "Login successful", "token": token}), 200

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
@jwt_required()
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

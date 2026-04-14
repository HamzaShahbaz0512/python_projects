from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'message':['Hello world']})

if(__name__=='__main__'):
    app.run(debug=True)
    

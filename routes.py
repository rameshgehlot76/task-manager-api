from flask import Blueprint, jsonify, request 
from database import db
from models import Task 

task_bp = Blueprint('tasks', __name__) 


# GET all tasks
@task_bp.route('/tasks', methods=['GET']) 
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200 


# GET single task
@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': f'Task {task_id} not found'}), 404
    return jsonify(task.to_dict()), 200 


# POST create task
@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400  
    
    if len(data['title'].strip()) == 0:
        return jsonify({'error': 'Title cannot be empty'}), 400
    
    task = Task(title=data['title'].strip())
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


# PUT update task 
@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])  
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': f'Task {task_id} not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if 'title' in data:
        if len(data['title'].strip()) == 0:
            return jsonify({'error': 'Title cannot be empty'}), 400
        task.title = data['title'].strip()
        
    if 'done' in data:
        if not isinstance(data['done'], bool):
            return jsonify({'error': 'done must be true or false'})
        task.done = data['done'] 
        
    db.session.commit()
    return jsonify(task.to_dict()), 200 


# DELETE task
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE']) 
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': f'Task {task_id} not found'}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': f'Task {task_id} deleted successfully'}), 200


    
    
    
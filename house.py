import json
from flask import Flask, request, jsonify

app = Flask(__name__)

class Task:
    def __init__(self, name, description, price, completed=False):
        self.name = name
        self.description = description
        self.price = price
        self.completed = completed

class Expense:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date

class FamilyMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class HouseholdManager:
    def __init__(self):
        self.tasks = []
        self.expenses = []
        self.family_members = []
        self.family_salary = 0

# Create an instance of HouseholdManager
household_manager = HouseholdManager()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = household_manager.view_tasks()
    return jsonify(tasks)

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = household_manager.view_expenses()
    return jsonify(expenses)

@app.route('/family_members', methods=['GET'])
def get_family_members():
    family_data = household_manager.view_family_members()
    return jsonify(family_data)

@app.route('/add_family_member', methods=['POST'])
def add_family_member():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    household_manager.add_family_member(name, age)
    return "Family member added", 201

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = float(data.get('price'))
    household_manager.add_task(name, description, price)
    return "Task added", 201

@app.route('/complete_task', methods=['POST'])
def complete_task():
    data = request.json
    task_name = data.get('task_name')
    household_manager.complete_task(task_name)
    return "Task completed", 200

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    name = data.get('name')
    amount = float(data.get('amount'))
    date = data.get('date')
    result = household_manager.add_expense(name, amount, date)
    if result == "Expense exceeds the available budget. Cannot add expense.":
        return "Expense exceeds the available budget", 400
    return "Expense added", 201

if __name__ == '__main__':
    app.run(debug=True)
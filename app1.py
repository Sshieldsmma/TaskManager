from flask import Flask, render_template, request, redirect, flash, url_for
'''Basic Flask application to manage tasks, user can add, delete, complete and delete all tasks'''
app1 = Flask(__name__)
app1.secret_key = "secrecy"

tasks = []

#Home route
@app1.route('/')
def home():
    return render_template('index.html', tasks = tasks, enumerate = enumerate)

#add task
@app1.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    due_date = request.form.get('date')
    if task and due_date:
        tasks.append({'task' : task, 'date' : due_date, 'completed' : False})
        flash('Task added successfully', 'success')
    return redirect('/')

#delete task
@app1.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        flash('Task deleted successfully', 'danger')
    return redirect('/')

#mark task as complete
@app1.route('/complete/<int:task_id>')
def complete_task(task_id):
    if task_id < len(tasks):
        tasks[task_id]['completed'] = True
        flash('Task completed successfully', 'success')
    return redirect('/')

#delete all tasks
@app1.route('/delete_all')
def delete_all():
    tasks.clear()
    flash('All tasks deleted successfully', 'danger')
    return redirect('/')


if __name__ == '__main__':
    app1.run(debug=True)
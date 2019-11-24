from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView

from app import app, db, admin
from .models import Task

from .forms import TaskForm, DeadlineForm

admin.add_view(ModelView(Task, db.session))

@app.route("/")
def homepage():
        return render_template('index.html',
                               title='homepage',
                             )

@app.route('/create_task', methods=['GET','POST'])
def create_task():#create a task
    form = TaskForm()
    if form.validate_on_submit():
        t = Task( task_name = form.task_name.data, description=form.description.data, deadline=form.deadline.data, state="uncomplete")
        db.session.add(t)
        db.session.commit()
        return redirect('/tasks')

    return render_template('create_task.html',
                           title='Create Task',
                           form=form)

@app.route('/tasks', methods=['GET'])
def getAllTask():#to show all tasks
    tasks = Task.query.all()
    return render_template('task_list.html',
                           title='All Task',
                           tasks=tasks)

@app.route('/edit_task/<id>', methods=['GET','POST'])
def edit_task(id):#edit a task by a form
    task = Task.query.get(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        t = task
        t.task_name = form.task_name.data
        t.description = form.description.data
        t.deadline = form.deadline.data
        t.state = t.state
        db.session.commit()
        return redirect('/tasks')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)

@app.route('/delete_task/<id>', methods=['GET'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')


@app.route('/mark_task/<id>', methods=['GET','POST'])
def mark_task(id):#change the state of the task, the set of the state is {completed, uncompleted}
    task = Task.query.get(id)
    t = task
    if t.state == "complete":
        t.state = "uncomplete"
    else:
        t.state = "complete"
    db.session.commit()
    return redirect('/tasks')

@app.route('/all_complete_tasks', methods=['GET'])
def getAllCompleteTask():#show all completed task
    tasks = Task.query.filter(Task.state=='complete').all()#using the query()
    return render_template('task_list.html',
                           title='All Complete Task',
                           tasks=tasks)

@app.route('/all_uncomplete_tasks', methods=['GET'])
def getAllUncompleteTask():#show all uncompeleted task
    tasks = Task.query.filter(Task.state=='uncomplete').all()#using the query()
    return render_template('task_list.html',
                           title='All Uncomplete Task',
                           tasks=tasks)

@app.route('/search_by_deadline', methods=['GET','POST'])
def SearchByDeadline():#search
    form = DeadlineForm()
    if form.validate_on_submit():
        tasks = Task.query.filter(Task.deadline==form.deadline_search.data).all()#using the query()
        return render_template('task_list.html',
                           title='All Uncomplete Task',
                           tasks=tasks,form=form)
    return render_template('search_by_deadline.html',
                           title='Search By Deadline',
                           form=form)
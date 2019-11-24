from app import db

class Task (db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), index=True)#the name of the task, String
    description = db.Column(db.String(250), index=True)#the description of the task, String
    deadline = db.Column(db.Date)#the deadline of the task, Date
    state = db.Column(db.String(250),index=True)#state:{'complete','uncomplete'}

    def __repr__(self):
        return self.task_name
from app import app
from models import db,Task
from faker import Faker
with app.app_context():
    Task.query.delete()
    fake = Faker()
    tasks = []
    for _ in range(10):
        task= Task(name=fake.first_name(),description=fake.sentence())
        tasks.append(task)
    db.session.add_all(tasks)
    db.session.commit()
    
print("Seed Data Has been Added Successfully!!!")
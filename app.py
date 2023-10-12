from flask import Flask,render_template,url_for,redirect,request
from flask_restful import Api,Resource
from flask_migrate import Migrate
from models import db,Task
app = Flask(__name__)

app.config["SECRET_KEY"] = '11108d8161bc968085e0ee86'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate=Migrate(app,db)
api = Api(app)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        tasks = Task.query.all()
        return render_template("index.html",tasks=tasks)
    name = request.form["name"]
    description = request.form["description"]
    new_task = Task(name=name,description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/addtask",methods=["GET","POST"])
def Tasks():
    if request.method == "GET":
        return render_template("addtask.html")
        
    name = request.form["name"]
    description = request.form["description"]
    new_task = Task(name=name,description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))
    
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == "GET":
        return render_template("update.html",task=task)
    name= request.form["name"]
    description=request.form["description"]
    task.name = name
    task.description=description
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.filter_by(id=id).first()
    
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(port=8000)
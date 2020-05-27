import os
from  flask  import  Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid  import ObjectId


from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.getenv("MONGO_URI_TM")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route("/add_task")
def add_task():
    return render_template("addtask.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=os.environ.get("PORT"), debug=True)


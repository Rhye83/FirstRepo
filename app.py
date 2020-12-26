import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#@app.route("/get_tasks")
#def get_tasks():
#    tasks = mongo.db.tasks.find()
#    return render_template("tasks.html", tasks = tasks)

@app.route("/")
def hello():
    return "Hello Word!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)

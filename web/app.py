import os
import logging
from flask import Flask, request
import mysql.connector


# logging
log_dir = "/app/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)

app = Flask(__name__)


def db():
    # environment variables for database connection
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
    )


@app.route("/")
def index():
    logging.info("Index page accessed")
    return """
        <h1>Todo API</h1>
        <form action="/add_from_browser" method="post">
            <input type="text" name="task" placeholder="Enter a task" required>
            <button type="submit">Add Task</button>
        </form>
        <br>
        <a href="/list"><button>View All Tasks</button></a>
    """


# helper route to add elements form the browser
@app.route("/add_from_browser", methods=["POST"])
def add_from_browser():
    t = request.form.get("task")
    c = db()
    cur = c.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (t,))
    c.commit()
    c.close()
    return f'Added "{t}"! <a href="/">Go back</a>'


# health check
@app.route("/health")
def health():
    return "ok"


# endpoint to add
@app.route("/add", methods=["POST"])
def add():
    t = request.json["task"]
    c = db()
    cur = c.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (t,))
    c.commit()
    c.close()
    return "added"


# endpoint to view records
@app.route("/list")
def list_all():
    c = db()
    cur = c.cursor()
    cur.execute("SELECT * FROM todos")
    r = cur.fetchall()
    c.close()
    return str(r)


# endpoint to delete
@app.route("/delete/<int:i>")
def delete(i):
    c = db()
    cur = c.cursor()
    cur.execute("DELETE FROM todos WHERE id=%s", (i,))
    c.commit()
    c.close()
    return "deleted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')  # replace with your database
    return conn

@app.route("/sqli-06/BenchmarkTest02729", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02729")
        bar = do_something(param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            return render_template("results.html", results=results)  # assuming results.html exists
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("benchmark_test.html")  # assuming benchmark_test.html exists

def do_something(param):
    bar = "safe!"
    map_data = {}
    map_data["keyA-87005"] = "a-Value"
    map_data["keyB-87005"] = param
    map_data["keyC"] = "another-Value"
    bar = map_data.get("keyB-87005")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

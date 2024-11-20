
from flask import Flask, request, render_template
import sqlite3
from contextlib import closing

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-04/BenchmarkTest02169", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get('BenchmarkTest02169', "")
        bar = do_something(param)

        sql = "{call " + bar + "}"

        try:
            with closing(database_con()) as connection:
                cursor = connection.cursor()
                cursor.execute(sql)
                rs = cursor.fetchall()
                print_results(rs, sql)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

def database_con():
    return sqlite3.connect('your_database.db')

def print_results(rs, sql):
    for row in rs:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

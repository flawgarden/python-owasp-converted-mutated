
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02543", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.form.getlist("BenchmarkTest02543")
    param = values[0] if values else ""

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')  # Update with your database path
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print_results(rows, response)
        conn.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

def print_results(rows, response):
    output = "<table><tr><th>Username</th><th>Password</th></tr>"
    for row in rows:
        output += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
    output += "</table>"
    response.data = output

if __name__ == "__main__":
    app.run(host='0.0.0.0')

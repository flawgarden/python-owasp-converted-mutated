
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02364", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        if flag:
            values = request.args.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest02364":
                        param = name
                        flag = False

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        connection = sqlite3.connect('database.db')  # Adjust the database path accordingly
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("results.html", results=results)  # Assuming you have a results.html for displaying results
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
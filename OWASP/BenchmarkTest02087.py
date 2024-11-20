
import urllib.parse
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02087", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.getlist("BenchmarkTest02087")

    if headers:
        param = headers[0]  # just grab the first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql, ('foo',))
        results = cursor.fetchall()
        print_results(results)
    except sqlite3.Error as e:
        return "Error processing request."

    return render_template("index.html")

def do_something(param):
    # This is a placeholder for the actual implementation
    # In the actual implementation, this would call an external thing interface
    return param

def print_results(results):
    # This function would render the results
    print(results)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

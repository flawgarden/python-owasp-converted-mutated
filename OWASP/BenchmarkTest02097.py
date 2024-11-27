
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02097", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request()

    return render_template("index.html")

def handle_request():
    response = "text/html;charset=UTF-8"
    param = ""
    headers = request.headers.get('BenchmarkTest02097')

    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)
    except sqlite3.Error as e:
        return "Error processing request."

    return response

def do_something(param):
    bar = "safe!"
    map94015 = {}
    map94015["keyA-94015"] = "a_Value"  # put some stuff in the collection
    map94015["keyB-94015"] = param       # put it in a collection
    map94015["keyC"] = "another_Value"   # put some stuff in the collection
    bar = map94015["keyB-94015"]          # get it back out
    bar = map94015["keyA-94015"]          # get safe value back out

    return bar

def print_results(results, sql):
    # Placeholder for result printing logic
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')

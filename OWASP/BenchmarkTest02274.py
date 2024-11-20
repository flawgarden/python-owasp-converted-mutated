
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-04/BenchmarkTest02274", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest02274", "")

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
    try:
        results = query(sql)
        response_text = "Your results are: "
        for s in results:
            response_text += escape_html(s) + "<br>"
    except sqlite3.Error as e:
        response_text = "No results returned for query: " + escape_html(sql)

    return response_text

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def query(sql):
    # Placeholder for the database query logic
    # Replace with actual database logic
    return []

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

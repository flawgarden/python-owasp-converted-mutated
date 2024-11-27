
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, param_name):
        return self.request.args.get(param_name)

def getSqlStatement():
    conn = sqlite3.connect('database.db')  # Change to your database configuration
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00680", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return render_template("index.html")

def handle_request(request):
    response = app.response_class(content_type="text/html;charset=UTF-8")

    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00680")
    if param is None:
        param = ""

    bar = "safe!"
    map33558 = {
        "keyA-33558": "a_Value",
        "keyB-33558": param,
        "keyC": "another_Value"
    }
    
    bar = map33558.get("keyB-33558")
    bar = map33558.get("keyA-33558")

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn, cursor = getSqlStatement()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(cursor, sql, response)
        conn.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def print_results(cursor, sql, response):
    response.data = f"Executed SQL: {sql} | Results: {cursor.fetchall()}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

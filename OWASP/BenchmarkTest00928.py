
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, key):
        return self.request.args.get(key)

@app.route("/sqli-01/BenchmarkTest00928", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00928")

    bar = ""
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql, ("foo",))
        response += str(statement.fetchall())
    except sqlite3.Error as e:
        response += "Error processing request."
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

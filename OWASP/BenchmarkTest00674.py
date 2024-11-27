
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, name):
        return self.request.args.get(name)

class DatabaseHelper:
    @staticmethod
    def getSqlConnection():
        return sqlite3.connect('database.db')  # Replace with your database

    @staticmethod
    def printResults(statement, sql, response):
        results = statement.fetchall()
        for row in results:
            response.write(f"{row}<br/>")

@app.route("/sqli-01/BenchmarkTest00674", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00674")
    if param is None:
        param = ""

    a55926 = param
    b55926 = a55926 + " SafeStuff"
    b55926 = b55926[:-1] + "Chars"

    map55926 = {}
    map55926["key55926"] = b55926
    c55926 = map55926["key55926"]
    d55926 = c55926[:-1]

    e55926 = base64.b64decode(base64.b64encode(d55926.encode())).decode()
    f55926 = e55926.split(" ")[0]

    thing = "barbarians_at_the_gate"

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + thing + "'"

    try:
        connection = DatabaseHelper.getSqlConnection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        DatabaseHelper.printResults(statement, sql, response)
        connection.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

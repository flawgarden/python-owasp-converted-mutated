
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class ThingInterface:
    @staticmethod
    def doSomething(param):
        return param[::-1]  # Sample transformation, adjust as needed.

class DatabaseHelper:
    @staticmethod
    def getSqlStatement():
        conn = sqlite3.connect('database.db')
        return conn.cursor()

    @staticmethod
    def outputUpdateComplete(sql, response):
        response.get_writer().println("Update Complete: " + sql)

@app.route("/sqli-00/BenchmarkTest00204", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = request.headers.get("BenchmarkTest00204", "")
    param = urllib.parse.unquote(param)

    thing = ThingInterface()
    bar = thing.doSomething(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

    try:
        statement = DatabaseHelper.getSqlStatement()
        statement.execute(sql, (bar,))
        DatabaseHelper.outputUpdateComplete(sql, response)
    except sqlite3.DatabaseError as e:
        response.set_data("Error processing request.")
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

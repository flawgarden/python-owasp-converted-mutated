
import os
import urllib.parse
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:
    @staticmethod
    def get_sql_statement():
        conn = sqlite3.connect('example.db')
        return conn.cursor()

    @staticmethod
    def output_update_complete(sql, response):
        response.get_writer().println(f"Executed SQL: {sql}")

class ThingInterface:
    def do_something(self, value):
        return f"Processed {value}"

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

@app.route("/sqli-00/BenchmarkTest00206", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = request.response
    param = request.headers.get("BenchmarkTest00206", "")
    
    param = urllib.parse.unquote(param)

    a13396 = param
    b13396 = a13396 + " SafeStuff"
    b13396 = b13396[:-5] + "Chars"
    
    map13396 = {}
    map13396["key13396"] = b13396
    c13396 = map13396["key13396"]
    d13396 = c13396[:-1]
    e13396 = base64.b64decode(base64.b64encode(d13396.encode())).decode()
    f13396 = e13396.split(" ")[0]

    thing = ThingFactory.create_thing()
    g13396 = "barbarians_at_the_gate"
    bar = thing.do_something(g13396)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        statement = DatabaseHelper.get_sql_statement()
        statement.execute(sql)
        DatabaseHelper.output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.get_writer().println("Error processing request.")
        return

if __name__ == "__main__":
    app.run(host='0.0.0.0')

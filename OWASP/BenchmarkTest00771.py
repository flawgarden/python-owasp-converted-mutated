
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00771", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = []
    values = request.args.getlist("BenchmarkTest00771")
    param = values[0] if values else ""

    bar = "safe!"
    map49960 = {}
    map49960["keyA-49960"] = "a-Value"
    map49960["keyB-49960"] = param
    map49960["keyC"] = "another-Value"
    bar = map49960["keyB-49960"]

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        return render_template("results.html", results=response)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

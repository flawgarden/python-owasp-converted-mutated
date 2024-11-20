
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02268", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.form.get('BenchmarkTest02268', '')

        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='{}'".format(bar)

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            connection.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

def do_something(param):
    bar = "safe!"
    map95440 = {}
    map95440["keyA-95440"] = "a_Value"
    map95440["keyB-95440"] = param
    map95440["keyC"] = "another_Value"
    bar = map95440["keyB-95440"]
    bar = map95440["keyA-95440"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

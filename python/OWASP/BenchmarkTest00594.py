
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00594", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00594":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "safe!"
    map29056 = {
        "keyA-29056": "a-Value",
        "keyB-29056": param,
        "keyC": "another-Value"
    }
    bar = map29056["keyB-29056"]

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='{}'".format(bar)

    try:
        connection = sqlite3.connect('database.db')  # Adjust connection method as needed
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        connection.close()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

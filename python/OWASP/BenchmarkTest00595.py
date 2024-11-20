
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00595", methods=['GET', 'POST'])
def benchmark_test_00595():
    if request.method == 'GET':
        return benchmark_test_00595_post()
    return benchmark_test_00595_post()

def benchmark_test_00595_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00595":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = (7 * 42) - 106
    bar = "This should never happen" if bar > 200 else param

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        # Placeholder for DatabaseHelper.printResults
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

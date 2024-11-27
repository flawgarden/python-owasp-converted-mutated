
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-00/BenchmarkTest00436", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest00436", "")

        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

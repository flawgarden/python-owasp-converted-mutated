
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02186", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02186", "")
        bar = do_something(request, param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            connection = sqlite3.connect('database.db')  # Update with your database
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            connection.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

def do_something(request, param):
    # Placeholder for actual implementation
    return param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
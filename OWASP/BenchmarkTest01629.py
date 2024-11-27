
from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-03/BenchmarkTest01629", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist("BenchmarkTest01629")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

        try:
            statement = get_sql_statement()
            statement.execute(sql, (bar,))
            statement.connection.commit()
            return "Update complete"
        except sqlite3.Error:
            return "Error processing request."

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

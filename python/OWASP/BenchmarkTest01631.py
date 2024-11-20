
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01631", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    values = request.values.getlist("BenchmarkTest01631")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql, (bar,))
        conn.commit()
        cursor.close()
        return "Update complete"
    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, param):
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

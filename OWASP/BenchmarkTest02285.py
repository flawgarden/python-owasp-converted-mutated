
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-05/BenchmarkTest02285", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get('BenchmarkTest02285', '')
        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            conn.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

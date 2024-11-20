
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Change to your database file
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-06/BenchmarkTest02732", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02732", '')

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        conn = get_db_connection()
        results = conn.execute(sql).fetchall()
        conn.close()

        response = "Your results are: <br>"
        for row in results:
            response += f"{row['USERNAME']}<br>"
        return response

    except sqlite3.Error as e:
        return f"Error processing request: {str(e)}"

def do_something(param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

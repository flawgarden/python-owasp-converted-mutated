
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00516", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00516', '')

    bar = ""
    guess = "ABC"
    switchTarget = guess[2]

    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bobs_your_uncle"
    elif switchTarget in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(cursor, sql)
        conn.close()
    except sqlite3.Error as e:
        return "Error processing request."

    return render_template("index.html")

def print_results(cursor, sql):
    results = cursor.fetchall()
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

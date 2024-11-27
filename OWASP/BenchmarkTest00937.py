
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Connect to your database
    return conn.cursor()

@app.route("/sqli-02/BenchmarkTest00937", methods=['GET', 'POST'])
def benchmark_test_00937():
    if request.method == 'GET':
        return benchmark_test_00937_post()
    return benchmark_test_00937_post()

def benchmark_test_00937_post():
    param = request.args.get('BenchmarkTest00937', '')

    bar = None
    guess = "ABC"
    switch_target = guess[1]  # Condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        rows = statement.fetchall()
        for row in rows:
            print(row)  # You can render this in a response as needed
        return render_template("results.html", rows=rows)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == '__main__':
    app.run(host='0.0.0.0')

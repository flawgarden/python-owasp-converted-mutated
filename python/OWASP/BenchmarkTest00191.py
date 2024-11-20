
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    return sqlite3.connect('your_database.db')

@app.route("/sqli-00/BenchmarkTest00191", methods=['GET', 'POST'])
def benchmark_test():
    param = request.headers.get('BenchmarkTest00191', '')
    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    sql = "{call " + bar + "}"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("results.html", results=results, sql=sql)
    except sqlite3.Error as e:
        return "Error processing request.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')

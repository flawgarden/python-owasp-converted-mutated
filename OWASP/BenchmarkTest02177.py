
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_database(sql):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return None
    finally:
        conn.close()

@app.route("/sqli-04/BenchmarkTest02177", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02177", "")
        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        results = query_database(sql)
        
        if results is not None:
            output = "Your results are: "
            for row in results:
                output += f"{row[0]}<br>"
            return render_template("index.html", output=output)
        else:
            return render_template("index.html", output="No results returned for query: " + sql)

    return render_template("index.html")

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

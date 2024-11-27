
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01381", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest01381', '')

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('your_database.db')
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql)
    except sqlite3.Error as e:
        print("Error processing request.")

    return render_template("index.html")

class Test:

    def do_something(self, param):
        num = 106
        return "This should never happen" if (7 * 42) - num > 200 else param

def print_results(statement, sql):
    # Implement result printing logic here
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')

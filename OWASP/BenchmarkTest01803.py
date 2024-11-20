
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01803", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01803")

        bar = Test().do_something(request, param)

        sql = f"{{call {bar}}}"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql)
            rs = statement.fetchall()
            print_results(rs, sql)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = None
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

def get_sql_connection():
    # Replace with your database connection logic
    return sqlite3.connect('your_database.db')

def print_results(rs, sql):
    # Replace with your result printing logic
    for row in rs:
        print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01380", methods=['GET', 'POST'])
def benchmark_test_01380():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01380', '')

        bar = Test().do_something(request, param)

        sql = "{call " + bar + "}"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print_results(results, sql)
            return render_template("index.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        num = 106
        return "This_should_always_happen" if (7 * 18) + num > 200 else param

def get_sql_connection():
    return sqlite3.connect('your_database.db')

def print_results(results, sql):
    # Implement your result printing logic here
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

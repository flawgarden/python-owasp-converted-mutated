
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-02/BenchmarkTest01307", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01307', '')
        bar = Test().do_something(request, param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            connection.close()
            # Assuming a function to print results similar to the Java version
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."
    return render_template("form.html")

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

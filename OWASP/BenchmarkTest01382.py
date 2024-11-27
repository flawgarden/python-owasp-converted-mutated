
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01382", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01382', '')
        bar = Test().do_something(param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request.", 500

    return render_template("index.html")

class Test:
    def do_something(self, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

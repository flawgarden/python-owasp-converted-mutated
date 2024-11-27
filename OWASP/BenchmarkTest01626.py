
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01626", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist("BenchmarkTest01626")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            connection.commit()
            print(results)  # For demonstration purposes
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."
    return render_template("index.html")

class Test:
    def do_something(self, request, param):
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')

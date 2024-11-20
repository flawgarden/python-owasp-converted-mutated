
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01622", methods=['GET', 'POST'])
def benchmark_test_01622():
    if request.method == 'GET':
        return benchmark_test_01622_post()

    return benchmark_test_01622_post()

def benchmark_test_01622_post():
    values = request.form.getlist("BenchmarkTest01622")
    param = values[0] if values else ""

    bar = Test().do_something(param)
    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

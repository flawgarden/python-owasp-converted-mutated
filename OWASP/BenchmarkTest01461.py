
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01461", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01461":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('your_database.db')  # Adjust the database file as needed
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("results.html", results=results, sql=sql)
    except sqlite3.Error:
        return "Error processing request."

class Test:
    def do_something(self, param):
        bar = "safe!"
        map96401 = {
            "keyA-96401": "a_Value",
            "keyB-96401": param,
            "keyC": "another_Value"
        }
        bar = map96401.get("keyB-96401")  # get it back out
        bar = map96401.get("keyA-96401")  # get safe value back out
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

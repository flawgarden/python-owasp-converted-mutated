
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-02/BenchmarkTest01096", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01096", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo', '{}')".format(bar)

    try:
        conn = sqlite3.connect('database.db')  # Adjust as per your DB connection
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        output_update_complete(sql)
    except sqlite3.Error as e:
        return "Error processing request."

    return render_template("index.html")


class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar


def output_update_complete(sql):
    print("Update completed for SQL:", sql)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00602", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00602":
                    param = name
                    flag = False
                    break

    bar = "alsosafe"
    if param != "":
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    sql = f"SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='{bar}'"

    try:
        con = sqlite3.connect('database.db')  # Adjust the path to your database
        cur = con.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        con.close()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

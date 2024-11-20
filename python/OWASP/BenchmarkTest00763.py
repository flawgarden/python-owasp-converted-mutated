
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00763", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    values = request.args.getlist("BenchmarkTest00763")
    param = values[0] if values else ""

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

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('your_database.db')
        statement = connection.execute(sql, ('foo',))
        results = statement.fetchall()

        for result in results:
            response += str(result) + "<br>"

    except sqlite3.Error as e:
        response = "Error processing request."

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

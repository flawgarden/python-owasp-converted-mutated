
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02529", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        values = request.form.getlist("BenchmarkTest02529")
        param = values[0] if values else ""

        bar = do_something(request, param)

        sql = f"{{call {bar}}}"

        try:
            connection = sqlite3.connect('your_database.db')  # Use your database configuration
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print_results(results, sql, response)
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response
        return response

def do_something(request, param):
    bar = "safe!"
    map32022 = {
        "keyA-32022": "a_Value",
        "keyB-32022": param,
        "keyC": "another_Value"
    }
    bar = map32022["keyB-32022"]
    bar = map32022["keyA-32022"]
    return bar

def print_results(results, sql, response):
    for row in results:
        response.data += f"<p>{row}</p>"
    response.data += f"<p>Executed SQL: {sql}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

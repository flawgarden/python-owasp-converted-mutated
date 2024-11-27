
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00761", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist('BenchmarkTest00761')
        param = values[0] if values else ""

        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        sql = "{call " + bar + "}"

        try:
            connection = sqlite3.connect('database.db')  # Adjust connection as needed
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return render_template("results.html", results=results, sql=sql)
        except sqlite3.Error as e:
            return "Error processing request."
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00773", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.form.getlist("BenchmarkTest00773")
    param = values[0] if values else ""

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute(sql, (bar,))
        conn.commit()
        cursor.close()
        return render_template("index.html", message="Update complete")
    except sqlite3.Error as e:
        if True:  # Change as needed to determine if SQL errors should be hidden
            return response("Error processing request.")
        else:
            raise Exception(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

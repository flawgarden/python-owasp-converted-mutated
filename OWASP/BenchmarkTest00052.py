
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    return sqlite3.connect('your_database.db')

@app.route("/sqli-00/BenchmarkTest00052", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00052')
        sql = f"{{call {param}}}"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()

            # Placeholder for handling results
            # Replace the following line with actual result handling code
            return render_template("results.html", results=results)

        except sqlite3.Error as e:
            if True:  # replace with a condition for hiding SQL errors
                return "Error processing request."
            else:
                raise e

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

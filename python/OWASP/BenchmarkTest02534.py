
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-05/BenchmarkTest02534", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.getlist('BenchmarkTest02534')
        bar = param[0] if param else ""

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            return render_template("result.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

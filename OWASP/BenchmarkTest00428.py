
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')  # adjust path to your database
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-00/BenchmarkTest00428", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest00428", "")
        
        bar = ""
        if param:
            valuesList = []
            valuesList.append("safe")
            valuesList.append(param)
            valuesList.append("moresafe")

            valuesList.pop(0)

            bar = valuesList[0]

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_db_connection()
            statement = connection.execute(sql, ("foo",))
            results = statement.fetchall()
            connection.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

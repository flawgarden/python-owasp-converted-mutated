
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-00/BenchmarkTest00440", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00440', '')
        bar = "safe!"
        map67409 = {
            "keyA-67409": "a_Value",
            "keyB-67409": param,
            "keyC": "another_Value"
        }
        bar = map67409["keyB-67409"]
        bar = map67409["keyA-67409"]

        sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

        try:
            conn, cursor = get_sql_statement()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return render_template("index.html", message="Update Complete")
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

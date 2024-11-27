
import os
import urllib.parse
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')  # Update with your database details
    return conn

@app.route("/sqli-00/BenchmarkTest00330", methods=['GET', 'POST'])
def benchmark_test():
    param = ""
    if request.method == 'POST':
        headers = request.headers.getlist("BenchmarkTest00330")
        if headers:
            param = headers[0]  # just grab the first element

        param = urllib.parse.unquote(param)

        a55109 = param
        b55109 = a55109 + " SafeStuff"
        b55109 = b55109[:-5] + "Chars"

        map55109 = {}
        map55109["key55109"] = b55109
        c55109 = map55109["key55109"]
        d55109 = c55109[:-1]
        e55109 = base64.b64decode(base64.b64encode(d55109.encode())).decode()
        f55109 = e55109.split(" ")[0]

        bar = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
        
        sql = f"{{call {bar}}}"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()  # Adjust according to your database logic

            return render_template("results.html", results=results, sql=sql)

        except sqlite3.Error as e:
            return "Error processing request.", 500

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

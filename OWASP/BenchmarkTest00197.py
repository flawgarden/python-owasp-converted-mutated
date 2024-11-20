
import os
from flask import Flask, request, render_template
from flask import jsonify
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_database(sql):
    conn = sqlite3.connect('database.db')  # Replace with your database file
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return None
    finally:
        conn.close()

@app.route("/sqli-00/BenchmarkTest00197", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00197', '')

    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[1]

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    results = query_database(sql)
    response = "Your results are: <br>"

    if results:
        for row in results:
            response += f"{escape_html(row[0])}<br>"
    else:
        response += f"No results returned for query: {escape_html(sql)}"

    return response

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

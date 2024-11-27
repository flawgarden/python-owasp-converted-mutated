
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02630", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        query_string = request.query_string.decode('utf-8')
        paramval = "BenchmarkTest02630="
        param_loc = query_string.find(paramval)
        
        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest02630' in query string."

        param = query_string[param_loc + len(paramval):]
        ampersand_loc = query_string.find("&", param_loc)

        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]
        
        param = urllib.parse.unquote(param)

        bar = do_something(request, param)

        sql = f"{{call {bar}}}"

        try:
            connection = sqlite3.connect('your_database.db')
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            connection.commit()  
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."
    return render_template("index.html")

def do_something(request, param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01712", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01712="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01712' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = f"{{call {bar}}}"
    
    try:
        connection = sqlite3.connect('database.db')  # Replace with actual db connection
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return str(results)

    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map_6261 = {
            "keyA-6261": "a-Value", 
            "keyB-6261": param, 
            "keyC": "another-Value"
        }
        bar = map_6261["keyB-6261"]
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

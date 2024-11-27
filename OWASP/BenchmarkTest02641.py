
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02641", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02641="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        response.data = "getQueryString() couldn't find expected parameter 'BenchmarkTest02641' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        results = query_database(sql)
        response.data = "Your results are: "
        for s in results:
            response.data += f"{s}<br>"
    except Exception as e:
        response.data = f"No results returned for query: {escape_html(sql)}"
    return response

def do_something(param):
    bar = param
    return bar

def query_database(sql):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

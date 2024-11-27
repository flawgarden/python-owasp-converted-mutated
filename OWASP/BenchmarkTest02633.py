
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02633", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02633="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02633' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"
    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        print_results(cursor, sql)
        return results
    except sqlite3.DatabaseError:
        return "Error processing request."

def do_something(param):
    a12213 = param
    b12213 = a12213 + " SafeStuff"
    b12213 = b12213[:-1] + "Chars"  # replace the end content
    c12213 = b12213
    d12213 = c12213[:-1]
    e12213 = d12213.encode().decode('utf-8')  # B64 encode and decode it
    f12213 = e12213.split(" ")[0]
    
    thing = create_thing()
    g12213 = "barbarians_at_the_gate"
    bar = thing.do_something(g12213)

    return bar

def get_sql_connection():
    return sqlite3.connect('database.db')

def print_results(cursor, sql):
    # Logic to print results (or format output) goes here
    pass

def create_thing():
    class Thing:
        def do_something(self, input):
            return input  # This is just a placeholder for the actual implementation
    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

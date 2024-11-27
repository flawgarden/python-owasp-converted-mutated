
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01729", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01729="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01729' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = Test().do_something(request, param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')  # change to your database
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return render_template("results.html", results=results)
    except sqlite3.DatabaseError as e:
        return "Error processing request."

class Test:
    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

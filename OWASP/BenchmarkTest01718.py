
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    return sqlite3.connect('database.db')  # Replace with your actual database file

@app.route("/sqli-03/BenchmarkTest01718", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        query_string = request.query_string.decode()
        paramval = "BenchmarkTest01718="
        param_loc = query_string.find(paramval)

        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest01718' in query string."

        param = query_string[param_loc + len(paramval):]
        ampersand_loc = query_string.find("&", param_loc)
        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]

        param = urllib.parse.unquote(param)

        bar = Test().do_something(request, param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            for row in results:
                print(row)  # Modify as necessary to display results
            connection.close()
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = None
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

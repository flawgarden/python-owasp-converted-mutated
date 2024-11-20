
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    # Assuming you have a function to get the database connection
    con = sqlite3.connect('your_database.db')  # Update your database path
    return con

@app.route("/sqli-03/BenchmarkTest01719", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01719="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01719' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = param.find("&")
    if ampersand_loc != -1:
        param = param[:ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='{}'".format(bar)

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        # Assuming you have a helper to print results
        print_results(statement, sql)
        return render_template("index.html", results=results)  # Update with appropriate HTML rendering
    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def print_results(statement, sql):
    # Custom function to print out the SQL results, implement as needed
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


def get_sql_connection():
    # Implement your connection logic here
    return sqlite3.connect('your_database.db')


@app.route("/sqli-03/BenchmarkTest01717", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        query_string = request.query_string.decode()
        paramval = "BenchmarkTest01717="
        param_loc = query_string.find(paramval)

        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest01717' in query string."

        param = query_string[param_loc + len(paramval):]
        ampersand_loc = query_string.find("&", param_loc)
        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]

        param = urllib.parse.unquote(param)

        bar = Test().do_something(param)

        sql = f"SELECT * from USERS where USERNAME=? and PASSWORD='{bar}'"

        try:
            connection = get_sql_connection()
            statement = connection.execute(sql, ("foo",))
            results = statement.fetchall()
            # Implement your result printing logic here
            return str(results)  # Example of how you may return the results

        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")


class Test:
    
    def do_something(self, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

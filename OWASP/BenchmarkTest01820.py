
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:
    @staticmethod
    def get_sql_statement():
        conn = sqlite3.connect('database.db')
        return conn

    @staticmethod
    def output_update_complete(sql, response):
        response.get_clf().write("Update completed for query: " + sql)

@app.route("/sqli-04/BenchmarkTest01820", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.values.get("BenchmarkTest01820", None)
    bar = Test().do_something(request, param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','{}')".format(bar)

    try:
        statement = DatabaseHelper.get_sql_statement()
        cursor = statement.cursor()
        cursor.execute(sql)
        statement.commit()
        DatabaseHelper.output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.get_clf().write("Error processing request.")
        return response

    return response

class Test:
    def do_something(self, request, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.remove("safe")  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

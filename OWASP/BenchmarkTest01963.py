
import os
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01963", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01963", "")
    param = unquote(param)

    bar = do_something(param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Here you should call your database execution method
        # For example: DatabaseHelper.JDBCtemplate.batchUpdate(sql)
        response.data = f"No results can be displayed for query: {sql} <br> because the Spring batchUpdate method doesn't return results."
        response.content_type = "text/html;charset=UTF-8"
        return response
    except Exception as e:
        response.data = "Error processing request."
        return response

def do_something(param):
    bar = param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

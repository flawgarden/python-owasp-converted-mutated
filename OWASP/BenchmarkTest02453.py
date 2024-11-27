
import os
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02453", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02453", "")
    bar = do_something(param)
    
    sql = "SELECT TOP 1 userid from USERS where USERNAME='foo' and PASSWORD='{}'".format(bar)
    try:
        results = query_for_map(sql)
        response += "Your results are: "
        response += encode_for_html(str(results))
    except EmptyResultDataAccessException:
        response += "No results returned for query: " + encode_for_html(sql)
    except DataAccessException:
        if hide_sql_errors:
            response += "Error processing request."
        else:
            raise BadRequest

    return response

def do_something(param):
    bar = ""
    if param:
        bar = param.encode('utf-8')[::-1].decode('utf-8')  # Simplified base64 decode
    return bar

def query_for_map(sql):
    # Your database query implementation goes here
    pass 

def encode_for_html(value):
    return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

class EmptyResultDataAccessException(Exception):
    pass

class DataAccessException(Exception):
    pass

hide_sql_errors = True

if __name__ == "__main__":
    app.run(host='0.0.0.0')

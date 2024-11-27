
import os
from flask import Flask, request, render_template
from flask import jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01553", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    try:
        param = request.args.get("BenchmarkTest01553", "")
        bar = Test().do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Replace with actual database execution logic
        execute_sql(sql)
        return jsonify(message="No results can be displayed for query: " + sql), 200

    except Exception as e:
        return handle_exception(e)

class Test:

    def do_something(self, param):
        bar = "safe!"
        map99501 = {}
        map99501["keyA-99501"] = "a_Value"
        map99501["keyB-99501"] = param
        map99501["keyC"] = "another_Value"
        bar = map99501["keyB-99501"]
        bar = map99501["keyA-99501"]
        return bar

def execute_sql(sql):
    # Placeholder for actual database execution.
    pass

def handle_exception(e):
    if isinstance(e, Exception):
        return jsonify(message="Error processing request."), 500
    return jsonify(message="Unexpected error."), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

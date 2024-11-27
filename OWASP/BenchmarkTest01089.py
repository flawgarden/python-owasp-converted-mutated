
import os
from flask import Flask, request, render_template, escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01089", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01089", "")
    param = param  # No URL decoding needed in Python for headers

    bar = Test().do_something(param)

    sql = f"SELECT USERNAME from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        results = query_for_object(sql)
        return f"Your results are: {escape(str(results))}"
    except Exception as e:
        return f"Error processing request." if hide_sql_errors else str(e)

class Test:
    def do_something(self, param):
        bar = "safe!"
        map_ = {
            "keyA-11607": "a_Value",
            "keyB-11607": param,
            "keyC": "another_Value"
        }
        bar = map_.get("keyB-11607")
        bar = map_.get("keyA-11607")
        return bar

def query_for_object(sql):
    # Mock function to simulate database query
    # Replace with actual database interaction.
    if "SELECT" in sql:
        return "sample_user"  # Simulated result
    raise Exception("Database error")  # Simulated error case

hide_sql_errors = True

if __name__ == "__main__":
    app.run(host='0.0.0.0')

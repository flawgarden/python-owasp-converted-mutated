
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00468", methods=['GET', 'POST'])
def benchmark_test_00468():
    if request.method == 'GET':
        return benchmark_test_00468_post()

    return benchmark_test_00468_post()

def benchmark_test_00468_post():
    param = request.values.get('BenchmarkTest00468', '')
    bar = "safe!"
    map50379 = {}
    map50379["keyA-50379"] = "a_Value"
    map50379["keyB-50379"] = param
    map50379["keyC"] = "another_Value"
    bar = map50379["keyB-50379"]
    bar = map50379["keyA-50379"]

    # Here you would typically construct a response, avoiding using
    # unsafe content directly
    response = app.response_class(response=bar, status=200, mimetype='text/html')
    response.headers['X-XSS-Protection'] = '0'
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
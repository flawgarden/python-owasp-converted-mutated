
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00893", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"
    
    param = request.args.get("BenchmarkTest00893", "")
    
    bar = ""
    
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    response.headers["X-XSS-Protection"] = "0"
    length = 1
    if bar:
        length = len(bar)
        response.set_data(bar[:length])
    
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

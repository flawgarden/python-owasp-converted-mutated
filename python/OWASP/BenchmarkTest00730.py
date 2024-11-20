
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00730", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")
    
    values = request.values.getlist("BenchmarkTest00730")
    param = values[0] if values else ""

    bar = "safe!"
    map29173 = {
        "keyA-29173": "a_Value",
        "keyB-29173": param,
        "keyC": "another_Value"
    }
    bar = map29173.get("keyB-29173")
    bar = map29173.get("keyA-29173")
    
    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

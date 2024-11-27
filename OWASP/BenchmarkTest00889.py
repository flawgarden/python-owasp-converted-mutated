
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00889", methods=['GET', 'POST'])
def benchmark_test_00889():
    if request.method == 'GET':
        return benchmark_test_00889_post()

    return benchmark_test_00889_post()

def benchmark_test_00889_post():
    response_content_type = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest00889", "")
    
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    response = app.response_class(response=bar, status=200, content_type=response_content_type)
    response.headers["X-XSS-Protection"] = "0"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

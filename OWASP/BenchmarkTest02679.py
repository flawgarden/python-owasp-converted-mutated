
from flask import Flask, request, Response, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02679", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02679", "", type=str)
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]

    html_content = f"<!DOCTYPE html>\n<html>\n<body>\n<p>"
    html_content += f"Formatted like: {obj[0]} and {obj[1]}."
    html_content += "\n</p>\n</body>\n</html>"

    response.set_data(html_content)
    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

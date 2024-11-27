
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01924", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("Referer", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = make_response(render_template("index.html", content=bar))
    response.headers["X-XSS-Protection"] = "0"
    return response

def do_something(param):
    bar = urllib.parse.quote(param)  # simulate HTML escape
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

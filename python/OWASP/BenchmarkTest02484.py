
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02484", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers["X-XSS-Protection"] = "0"
        values = request.values.getlist("BenchmarkTest02484")
        param = values[0] if values else ""

        bar = do_something(param)

        response.data = bar.encode('utf-8')
        response.content_type = "text/html;charset=UTF-8"
        return response
    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map_12535 = {
        "keyA-12535": "a_Value",
        "keyB-12535": param,
        "keyC": "another_Value"
    }
    bar = map_12535["keyB-12535"]
    bar = map_12535["keyA-12535"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

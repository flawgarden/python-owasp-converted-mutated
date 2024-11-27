
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00722", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = "text/html;charset=UTF-8"

        values = request.values.getlist("BenchmarkTest00722")
        param = values[0] if values else ""

        bar = "safe!"
        map49442 = {
            "keyA-49442": "a_Value",
            "keyB-49442": param,
            "keyC": "another_Value"
        }
        bar = map49442.get("keyB-49442")
        bar = map49442.get("keyA-49442")

        response.headers['X-XSS-Protection'] = "0"
        obj = ["a", "b"]
        response.set_data(bar % tuple(obj))

        return response
    else:
        return benchmark_test()  # Call post method on GET request

if __name__ == "__main__":
    app.run(host='0.0.0.0')

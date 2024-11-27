
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00471", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response="",
        status=200,
        mimetype='text/html'
    )
    param = request.values.get('BenchmarkTest00471', '')

    bar = escape(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = "Formatted like: %s and %s." % ("a", bar)
    return response

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

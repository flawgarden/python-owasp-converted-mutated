
import urllib.parse
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00157", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("Referer", "")
    param = urllib.parse.unquote(param)

    # Simple ? condition that assigns param to bar on false condition
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

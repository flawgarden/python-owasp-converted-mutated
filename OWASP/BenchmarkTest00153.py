
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00153", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.headers.get("Referer"):
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map96050 = {
        "keyA-96050": "a-Value",
        "keyB-96050": param,
        "keyC": "another-Value"
    }
    bar = map96050.get("keyB-96050")

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

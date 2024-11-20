
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00289", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.headers.get('Referer', '')
        param = urllib.parse.unquote(param)

        bar = param  # In a real application, you would use an XSS protection library here

        response = Response(bar)
        response.headers['X-XSS-Protection'] = "0"
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

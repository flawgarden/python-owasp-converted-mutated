
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00290", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    sbxyz73567 = param + "_SafeStuff"
    response = make_response(sbxyz73567)
    response.headers['X-XSS-Protection'] = '0'

    return response

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')

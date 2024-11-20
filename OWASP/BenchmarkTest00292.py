
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00292", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        response = Response(content_type="text/html;charset=UTF-8")

        param = ""
        referer = request.headers.get("Referer")

        if referer:
            param = referer

        param = urllib.parse.unquote(param)

        bar = param
        if param and len(param) > 1:
            bar = param[:-1]

        response.headers["X-XSS-Protection"] = "0"
        length = 1
        if bar:
            length = len(bar)
            response.data = bar[:length]

        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

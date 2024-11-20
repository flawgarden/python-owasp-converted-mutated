
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00281", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        referer = request.headers.get('Referer')

        if referer:
            param = referer  # just grab first element

        # URL Decode the header value
        param = urllib.parse.unquote(param)

        bar = ""

        # Simple condition that assigns constant to bar on true condition
        num = 106

        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

        response.headers['X-XSS-Protection'] = '0'
        response.data = f"{bar}"
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/xss-01/BenchmarkTest00647", methods=['GET', 'POST'])
def benchmark_test_00647():
    if request.method == 'GET':
        return benchmark_test_00647_post(request)
    return benchmark_test_00647_post(request)

def benchmark_test_00647_post(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00647', '')  # Similar to scr.getTheParameter
    bar = escape_html(param)  # Function to encode for HTML (similar to ESAPI.encoder().encodeForHTML)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

def escape_html(text):
    from html import escape
    return escape(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

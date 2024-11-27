
from flask import Flask, request, session, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'

@app.route("/trustbound-00/BenchmarkTest01206", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    headers = request.headers.get("BenchmarkTest01206")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    session['userid'] = bar

    response.data = (
        "Item: 'userid' with value: '"
        + Utils.encode_for_html(bar)
        + "' saved in session."
    )
    
    return response

class Test:

    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            sbxyz14623 = list(param)
            sbxyz14623[-1] = 'Z'
            bar = ''.join(sbxyz14623)

        return bar

class Utils:
    @staticmethod
    def encode_for_html(value):
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

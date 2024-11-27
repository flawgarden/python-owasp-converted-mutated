
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        return self.escape_html(param)

    def escape_html(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.route("/securecookie-00/BenchmarkTest01187", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    header_value = request.headers.get('BenchmarkTest01187', None)

    if header_value:
        param = header_value

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    str_param = param if isinstance(param, str) else ""

    if str_param == "":
        str_param = "No cookie value supplied"

    response = make_response(render_template("index.html"))
    response.set_cookie("SomeCookie", str_param, secure=False, httponly=True, path=request.path)

    response.get_data = lambda: "Created cookie: 'SomeCookie': with value: '{}' and secure flag set to: {}".format(
        str_param, False)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, Response, make_response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = "safe!"
        map_97880 = {
            "keyA-97880": "a_Value",
            "keyB-97880": param,
            "keyC": "another_Value"
        }
        bar = map_97880["keyB-97880"]
        bar = map_97880["keyA-97880"]
        return bar

@app.route("/securecookie-00/BenchmarkTest01605", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    values = request.values.getlist("BenchmarkTest01605")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    str_input = param or "No cookie value supplied"
    cookie = f'SomeCookie={html.escape(str_input)}; Secure; HttpOnly; Path={request.path}'
    
    response = make_response(f"Created cookie: 'SomeCookie': with value: '{html.escape(str_input)}' and secure flag set to: true")
    response.headers.add('Set-Cookie', cookie)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

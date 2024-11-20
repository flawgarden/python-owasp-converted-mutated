
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01604", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    
    values = request.values.getlist("BenchmarkTest01604")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    str_val = param if isinstance(param, str) else ""
    if not str_val:
        str_val = "No cookie value supplied"
    
    cookie = ('SomeCookie', str_val, {'secure': True, 'httponly': True, 'path': request.path})
    response.set_cookie(*cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{str_val}' and secure flag set to: true"
    response.content_type = "text/html;charset=UTF-8"
    
    return response

class Test:
    def do_something(self, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01280", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest01280', '')
    bar = Test().do_something(param)

    str_value = param if isinstance(param, str) else "No cookie value supplied"
    response = make_response()
    cookie = ('SomeCookie', str_value)
    
    response.set_cookie(cookie[0], cookie[1], secure=False, httponly=True, path=request.path)
    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"
    
    return response

class Test:

    def do_something(self, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

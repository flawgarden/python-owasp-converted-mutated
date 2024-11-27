
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.route("/securecookie-00/BenchmarkTest01436", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01436":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    input_param = param
    str_ = "?" if isinstance(input_param, str) else ""
    if isinstance(input_param, str):
        str_ = input_param
    
    if str_ == "":
        str_ = "No cookie value supplied"

    cookie = make_response()
    cookie.set_cookie("SomeCookie", str_, secure=True, httponly=True, path=request.path)
    
    response_body = f"Created cookie: 'SomeCookie': with value: '{str_}' and secure flag set to: true"
    return response_body, 200, {'Set-Cookie': cookie.headers['Set-Cookie']}

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

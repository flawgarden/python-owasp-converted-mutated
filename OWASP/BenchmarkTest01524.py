
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, request, param):
        num = 106
        return "This_should_always_happen" if (7 * 18) + num > 200 else param

@app.route("/securecookie-00/BenchmarkTest01524", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest01524', "")
    bar = Test().do_something(request, param)

    response = make_response(render_template("index.html"))
    cookie = f"SomeCookie={bar}; Secure; HttpOnly; Path={request.path}"
    response.set_cookie("SomeCookie", bar, secure=True, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

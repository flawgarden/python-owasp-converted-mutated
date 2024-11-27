
from flask import Flask, request, make_response, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        num = 106
        return "This should never happen" if (7 * 42) - num > 200 else param

@app.route("/securecookie-00/BenchmarkTest01789", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get("BenchmarkTest01789", "")
    
    bar = Test().do_something(param)

    if not param:
        response.set_data("No cookie value supplied")
    else:
        cookie = make_response(f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: false")
        
        cookie.set_cookie("SomeCookie", bar, secure=False, httponly=True, path=request.path)
        response = cookie

    return response

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template("404.html"), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01281", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest01281', "")
    bar = Test().do_something(param)

    cookie_value = param if param else "No cookie value supplied"
    response = make_response(render_template("index.html"))
    response.set_cookie("SomeCookie", cookie_value, secure=False, httponly=True, path=request.path)

    return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

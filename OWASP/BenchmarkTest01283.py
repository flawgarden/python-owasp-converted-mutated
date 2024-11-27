
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01283", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    
    param = request.form.get("BenchmarkTest01283", "")
    bar = Test().do_something(request, param)

    str_value = param if isinstance(param, str) else ""
    if str_value == "":
        str_value = "No cookie value supplied"
    
    response.set_cookie("SomeCookie", str_value, secure=False, httponly=True, path=request.path)
    
    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"
    
    return response

class Test:

    def do_something(self, request, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        else:
            return "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

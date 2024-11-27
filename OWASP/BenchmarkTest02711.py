
from flask import Flask, request, make_response
import urllib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02711", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest02711")
    
    bar = do_something(param)

    if bar == "":
        bar = "No cookie value supplied"
    
    response = make_response("Created cookie: 'SomeCookie': with value: '" + urllib.parse.quote(bar) + "' and secure flag set to: true")
    response.set_cookie("SomeCookie", bar, secure=True, httponly=True, path=request.path)

    return response

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

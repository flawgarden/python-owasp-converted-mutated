
import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00565", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00565":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = param

    str_value = param if param else "No cookie value supplied"
    response = make_response("Created cookie: 'SomeCookie': with value: '" + bar + "' and secure flag set to: false")
    
    response.set_cookie("SomeCookie", str_value, secure=False, httponly=True, path=request.path)
    
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

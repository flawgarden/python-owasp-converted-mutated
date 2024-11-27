
import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00491", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.values.get("BenchmarkTest00491", "")
    
    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + "Z"

    cookie_value = bar if bar else "No cookie value supplied"
    response.set_cookie("SomeCookie", cookie_value, secure=False, httponly=True, path=request.path)

    response.body = f"Created cookie: 'SomeCookie': with value: '{cookie_value}' and secure flag set to: false"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

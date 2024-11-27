
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00300", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = ""
    if 'BenchmarkTest00300' in request.headers:
        param = request.headers['BenchmarkTest00300']

    param = base64.b64decode(base64.b64encode(param.encode())).decode()

    if param is None:
        param = "No cookie value supplied"

    cookie = ('SomeCookie', param)

    response.set_cookie(cookie[0], cookie[1], secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: '{cookie[0]}': with value: '{param}' and secure flag set to: False"

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

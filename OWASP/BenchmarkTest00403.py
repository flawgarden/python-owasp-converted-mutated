
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00403", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest00403', '')
    
    bar = "This_should_always_happen" if (7 * 18) + 106 > 200 else param

    cookie_value = bar if bar else "No cookie value supplied"
    response.set_cookie("SomeCookie", cookie_value, secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{cookie_value}' and secure flag set to: false"
    response.content_type = "text/html;charset=UTF-8"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

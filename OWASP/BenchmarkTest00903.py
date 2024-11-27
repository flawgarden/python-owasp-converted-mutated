
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00903", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get("BenchmarkTest00903")

    bar = None
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    if param is None:
        param = "No cookie value supplied"
    
    cookie = f"SomeCookie={param}; Path={request.path}; HttpOnly"
    response.headers.add('Set-Cookie', cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{param}' and secure flag set to: false"
    response.content_type = "text/html;charset=UTF-8"

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

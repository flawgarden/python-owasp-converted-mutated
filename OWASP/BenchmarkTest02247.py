
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02247", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get('BenchmarkTest02247', '') if request.method == 'GET' else request.form.get('BenchmarkTest02247', '')
    bar = do_something(param)

    cookie = f'SomeCookie={bar}; Path={request.path}; Secure; HttpOnly'
    response.headers.add('Set-Cookie', cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true"
    response.content_type = 'text/html;charset=UTF-8'

    return response

def do_something(param):
    bar = 'alsosafe'
    if param:
        values_list = ['safe', param, 'moresafe']
        values_list.pop(0)
        bar = values_list[1]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

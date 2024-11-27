
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route('/securecookie-00/BenchmarkTest00904', methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = request.args.get('BenchmarkTest00904')

    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    input_data = param if isinstance(param, str) else None
    if input_data is None:
        str_val = "No cookie value supplied"
    else:
        str_val = input_data

    cookie = ('SomeCookie', str_val, {'secure': True, 'httponly': True, 'path': request.path})
    response.set_cookie(*cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{str_val}' and secure flag set to: true"
    response.content_type = "text/html;charset=UTF-8"

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

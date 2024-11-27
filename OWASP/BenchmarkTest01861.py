
from flask import Flask, request, make_response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest01861", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("securecookie-00/BenchmarkTest01861.html"))
        user_cookie = ('BenchmarkTest01861', 'whatever', {'max_age': 60 * 3, 'secure': True, 'path': request.path, 'domain': request.host.split(':')[0]})
        response.set_cookie(*user_cookie)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest01861' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01861'])

        bar = do_something(param)

        cookie_value = bar if bar else "No cookie value supplied"
        response = make_response(f"Created cookie: 'SomeCookie': with value: '{cookie_value}' and secure flag set to: false")

        response.set_cookie('SomeCookie', cookie_value, secure=False, httponly=True, path=request.path)
        return response


def do_something(param):
    bar = param
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

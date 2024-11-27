
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00097", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("trustbound-00/BenchmarkTest00097.html"))
        user_cookie = make_response("Cookie created")
        user_cookie.set_cookie("BenchmarkTest00097", "color", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(':')[0])
        response.set_cookie("BenchmarkTest00097", "color", max_age=60 * 3, secure=True)
        return response
    
    else:
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest00097' in the_cookies:
            param = the_cookies['BenchmarkTest00097']

        bar = "This_should_always_happen" if (7 * 18) + 106 > 200 else param
        request.environ['werkzeug.session'][bar] = "10340"

        return (
            f"Item: '{bar}' with value: 10340 saved in session."
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

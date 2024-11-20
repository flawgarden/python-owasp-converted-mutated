
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00098", methods=['GET', 'POST'])
def benchmark_test_00098():
    if request.method == 'GET':
        response = make_response(render_template("trustbound-00/BenchmarkTest00098.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00098", "my_user_id", max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.headers.addlist('Set-Cookie', user_cookie.headers['Set-Cookie'])
        return response
    elif request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if "BenchmarkTest00098" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest00098"])

        bar = param # You may want to escape this when rendering to HTML later on

        # Storing in session
        request.environ['werkzeug.session'].set('userid', bar)

        return "Item: 'userid' with value: '{}' saved in session.".format(bar)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

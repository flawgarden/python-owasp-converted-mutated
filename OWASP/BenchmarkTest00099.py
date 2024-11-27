
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/trustbound-00/BenchmarkTest00099", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("trustbound-00/BenchmarkTest00099.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00099", "my_userid", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        resp.set_cookie("BenchmarkTest00099", "my_userid", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"

        if "BenchmarkTest00099" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest00099"])

        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.remove(values_list[0])  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        request.session['userid'] = bar
        return f"Item: 'userid' with value: '{bar}' saved in session."

if __name__ == '__main__':
    app.run(host='0.0.0.0')

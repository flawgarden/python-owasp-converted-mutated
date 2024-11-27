
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/trustbound-00/BenchmarkTest00993", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("trustbound-00/BenchmarkTest00993.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest00993=my_user_id; Max-Age=180; Secure; Path={}; Domain={}".format(
            request.path, request.host))
        resp.headers.add('Set-Cookie', user_cookie)
        return resp

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest00993' in the_cookies:
            param = the_cookies['BenchmarkTest00993']

        bar = Test().do_something(request, param)
        request.session['userid'] = bar

        return "Item: 'userid' with value: '{}' saved in session.".format(bar)


class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

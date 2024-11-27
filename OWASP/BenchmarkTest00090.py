
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00090", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("cmdi-00/BenchmarkTest00090.html"))
        user_cookie = make_response('BenchmarkTest00090', 'ls')
        resp.set_cookie('BenchmarkTest00090', user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp
    
    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00090' in the_cookies:
            param = the_cookies['BenchmarkTest00090']

        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        cmd = ""
        os_name = os.name
        if os_name == 'nt':
            cmd = "echo "

        try:
            process = os.popen(cmd + bar)
            output = process.read()
            return render_template("output.html", output=output)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", error_message=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

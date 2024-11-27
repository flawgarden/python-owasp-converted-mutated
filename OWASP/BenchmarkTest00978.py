
import os
from flask import Flask, request, render_template, make_response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        a60830 = param  
        b60830 = str(a60830) + " SafeStuff"
        b60830 = b60830[:-5] + "Chars"
        map60830 = {'key60830': b60830}
        c60830 = map60830['key60830']
        d60830 = c60830[:-1]  
        e60830 = base64.b64decode(base64.b64encode(d60830.encode())).decode()
        f60830 = e60830.split(" ")[0]
        return "barbarians_at_the_gate"

@app.route("/cmdi-01/BenchmarkTest00978", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00978.html"))
        user_cookie = request.cookies.get('BenchmarkTest00978', 'localhost')
        response.set_cookie('BenchmarkTest00978', user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(":")[0])
        return response
    
    if request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if the_cookies:
            for key, value in the_cookies.items():
                if key == "BenchmarkTest00978":
                    param = value
                    break

        bar = Test().do_something(param)

        cmd = ""
        a1 = ""
        a2 = ""

        if os.name == 'nt':
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = f"echo {bar}"
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = f"ping -c1 {bar}"

        try:
            process = os.popen(f"{a1} {a2} {cmd}")
            result = process.read()
            return result
        except Exception as e:
            return f"Problem executing cmdi - TestCase: {str(e)}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

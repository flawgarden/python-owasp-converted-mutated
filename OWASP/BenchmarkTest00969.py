
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00969", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00969.html"))
        user_cookie = ('BenchmarkTest00969', 'ECHOOO', 60 * 3)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00969' in the_cookies:
            param = the_cookies['BenchmarkTest00969']

        bar = Test().do_something(request, param)

        arg_list = []
        if os.name == 'nt':
            arg_list.append("cmd.exe")
            arg_list.append("/c")
        else:
            arg_list.append("sh")
            arg_list.append("-c")
        arg_list.append("echo " + bar)

        process = os.popen(' '.join(arg_list))
        output = process.read()
        process.close()

        return output

class Test:
    def do_something(self, request, param):
        a10263 = param
        b10263 = a10263 + " SafeStuff"
        b10263 = b10263[:-len("Chars")] + "Chars"
        map10263 = {}
        map10263["key10263"] = b10263
        c10263 = map10263["key10263"]
        d10263 = c10263[:-1]
        e10263 = base64.b64decode(base64.b64encode(d10263.encode())).decode()
        f10263 = e10263.split(" ")[0]
        thing = ThingFactory.create_thing()
        g10263 = "barbarians_at_the_gate"
        bar = thing.do_something(g10263)

        return bar

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

class ThingInterface:
    def do_something(self, input):
        return input

if __name__ == "__main__":
    app.run(host='0.0.0.0')

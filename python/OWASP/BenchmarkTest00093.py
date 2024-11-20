
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00093", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("cmdi-00/BenchmarkTest00093.html"))
        user_cookie = ('BenchmarkTest00093', 'ls', 60 * 3, request.path)
        resp.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=user_cookie[3], domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if cookies:
            param = cookies.get("BenchmarkTest00093", param)

        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        cmd = ""
        if os.name == 'nt':  # Check if the OS is Windows
            cmd = "echo "  # Using echo command for Windows

        args_env = {"Foo": "bar"}

        try:
            process = os.popen(cmd + bar)
            output = process.read()
            return render_template("output.html", output=output)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", message=urllib.parse.quote(str(e)))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

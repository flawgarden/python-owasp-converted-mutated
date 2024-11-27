
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-02/BenchmarkTest01865", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-02/BenchmarkTest01865.html"))
        user_cookie = ('BenchmarkTest01865', 'ls', 60 * 3) # Cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01865' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01865'])

        bar = do_something(request, param)

        cmd = ""
        os_name = os.name
        if os_name == 'nt':
            cmd = "echo"  # Adjust based on the actual command to be executed

        args_env = {"Foo": "bar"}

        try:
            process = os.popen(cmd + bar)  # Adjust command execution if necessary
            output = process.read()
            return output  # Return the output of the command
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return f"Error: {str(e)}"

def do_something(request, param):
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


import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01864", methods=['GET'])
def benchmark_get():
    resp = make_response(render_template("cmdi-02/BenchmarkTest01864.html"))
    user_cookie = ('BenchmarkTest01864', 'ls', 60 * 3, True)
    resp.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3])
    return resp

@app.route("/cmdi-02/BenchmarkTest01864", methods=['POST'])
def benchmark_post():
    cookies = request.cookies
    param = "noCookieValueSupplied"
    
    if 'BenchmarkTest01864' in cookies:
        param = cookies['BenchmarkTest01864']

    bar = do_something(request, param)
    cmd = ""
    
    if os.name == 'nt':
        cmd = "echo "  # Windows command

    args_env = ['Foo=bar']
    
    try:
        process = os.popen(cmd + bar)  # run the command
        output = process.read()  # get the output
        process.close()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return f"Error: {str(e)}"

def do_something(request, param):
    bar = param
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

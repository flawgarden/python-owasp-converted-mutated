
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00310", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")
    param = ""
    headers = request.headers.getlist("BenchmarkTest00310")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)  # URL Decode the header value

    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = 'echo '

    args_env = {"Foo": "bar"}
    try:
        p = os.popen(cmd + bar)
        output = p.read()
        response.data = output
        p.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

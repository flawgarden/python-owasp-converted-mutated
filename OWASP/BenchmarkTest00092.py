
import os
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00092", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-00/BenchmarkTest00092.html"))
        user_cookie = 'FOO%3Decho+Injection'
        response.set_cookie("BenchmarkTest00092", user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00092" in cookies:
            param = cookies.get("BenchmarkTest00092")

        bar = None
        guess = "ABC"
        switch_target = guess[2]  # 'C'

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        cmd = os.popen('echo').read().strip()  # Replace with actual command retrieval
        args = [cmd]
        args_env = [bar]

        try:
            process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
            response = process.read()
            return response
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return f"Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

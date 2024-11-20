
from flask import Flask, request, render_template, make_response
import hashlib
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00961", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-01/BenchmarkTest00961.html"))
        user_cookie = ("BenchmarkTest00961", "someSecret", 60 * 3, True)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3], path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00961' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00961'])

        bar = Test().do_something(param)

        input_data = bar.encode() if isinstance(bar, str) else bytes(bar)
        sha1_hash = hashlib.sha1(input_data).hexdigest()

        file_target = os.path.join('passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + sha1_hash + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

class Test:

    def do_something(self, param):
        bar = "safe!"
        map47722 = {"keyA-47722": "a_Value", "keyB-47722": param, "keyC": "another_Value"}
        bar = map47722["keyB-47722"]
        bar = map47722["keyA-47722"]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

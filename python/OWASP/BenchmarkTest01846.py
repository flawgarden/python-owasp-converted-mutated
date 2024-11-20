
import os
from flask import Flask, request, render_template, make_response
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-02/BenchmarkTest01846", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-02/BenchmarkTest01846.html"))
        user_cookie = "someSecret"
        response.set_cookie("BenchmarkTest01846", user_cookie, max_age=60 * 3, secure=True, path=request.path,
                            domain=request.host)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest01846" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest01846"])

        bar = do_something(param)

        try:
            input_bytes = b'?'
            input_param = bar.encode('utf-8')

            hasher = hashlib.sha1()
            hasher.update(input_param)

            result = hasher.digest()
            file_target = os.path.join("testfiles", "passwordFile.txt")
            with open(file_target, "a") as fw:
                fw.write("hash_value=" + result.hex() + "\n")

            return f"Sensitive value '{input_param.decode('utf-8')}' hashed and stored<br/>"
        except Exception as e:
            print("Problem executing hash - TestCase hashlib.sha1()")
            raise Exception(e)
    return "Hash Test executed"


def do_something(param):
    bar = param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

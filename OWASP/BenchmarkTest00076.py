
import os
import hashlib
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00076", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("hash-00/BenchmarkTest00076.html"))
        user_cookie = ('BenchmarkTest00076', 'someSecret', 180)  # Store cookie for 3 minutes
        resp.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00076' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00076'])

        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ('C', 'D'):
            bar = param
        else:
            bar = "bobs_your_uncle"

        try:
            algorithm = "SHA5"  # Default to SHA5, can load from properties if needed
            md = hashlib.new(algorithm)
            input_data = bytes(bar, 'utf-8')
            md.update(input_data)

            result = md.digest()
            file_target = os.path.join(os.path.dirname(__file__), "passwordFile.txt")
            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + result.decode('latin1') + "\n")  # For Base64 encode use `base64`

            return f"Sensitive value '{input_data.decode('utf-8')}' hashed and stored<br/>" + \
                   "Hash Test executed"
        except Exception as e:
            print("Problem executing hash - TestCase")
            return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

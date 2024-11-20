
import os
import hashlib
from urllib.parse import unquote
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00073", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-00/BenchmarkTest00073.html"))
        user_cookie = make_response("someSecret")
        response.set_cookie('BenchmarkTest00073', 'someSecret', max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00073' in the_cookies:
            param = unquote(the_cookies['BenchmarkTest00073'])

        bar = ""
        guess = "ABC"
        switch_target = guess[1]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        input_data = bytes('?', 'utf-8')
        if isinstance(bar, str):
            input_data = bar.encode()

        md = hashlib.md5()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_testfiles_dir", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>Hash Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

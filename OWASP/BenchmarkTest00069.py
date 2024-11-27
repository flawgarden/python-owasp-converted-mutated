
import os
from flask import Flask, request, render_template, make_response
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00069", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-00/BenchmarkTest00069.html"))
        user_cookie = {
            'name': 'BenchmarkTest00069',
            'value': 'someSecret',
            'max_age': 60 * 3,
            'secure': True,
            'path': request.path,
            'domain': request.host.split(':')[0]
        }
        response.set_cookie(user_cookie['name'], user_cookie['value'], max_age=user_cookie['max_age'], 
                            secure=user_cookie['secure'], path=user_cookie['path'], domain=user_cookie['domain'])
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00069' in cookies:
            param = cookies['BenchmarkTest00069']

        bar = param if (7 * 18) + 106 <= 200 else "This_should_always_happen"
        input_value = b'?'

        md = hashlib.new('sha384')
        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')

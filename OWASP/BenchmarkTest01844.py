
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01844", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        user_cookie = make_response(render_template("hash-02/BenchmarkTest01844.html"))
        user_cookie.set_cookie("BenchmarkTest01844", "someSecret", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(':')[0])
        return user_cookie

    elif request.method == 'POST':
        param = request.cookies.get('BenchmarkTest01844', 'noCookieValueSupplied')

        bar = do_something(param)

        try:
            input_bytes = b'?'
            if isinstance(bar, str):
                input_bytes = bar.encode()
            md = hash_function(input_bytes)

            file_target = os.path.join('path_to_testfiles_dir', 'passwordFile.txt')
            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + base64.b64encode(md).decode() + "\n")

            return f"Sensitive value '{escape_html(str(input_bytes))}' hashed and stored<br/>"
            
        except Exception as e:
            print("Problem executing hash - TestCase failed")
            return str(e)

def do_something(param):
    a37183 = param
    b37183 = a37183 + " SafeStuff"
    c37183 = b37183[:-1]
    e37183 = base64.b64decode(base64.b64encode(c37183.encode())).decode()
    f37183 = e37183.split(" ")[0]

    bar = "barbarians_at_the_gate"  # Static so this whole flow is 'safe'
    # call the reflection or object creation logic here as necessary
    return bar

def hash_function(input_bytes):
    import hashlib
    return hashlib.sha1(input_bytes).digest()

def escape_html(text):
    from html import escape
    return escape(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

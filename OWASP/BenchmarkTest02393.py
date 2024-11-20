
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02393", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "Content-Type: text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest02393', "")
    bar = do_something(param)

    algorithm = "SHA512"
    md = hashlib.new(algorithm)
    input_param = bar.encode()
    md.update(input_param)

    result = md.digest()
    file_target = 'passwordFile.txt'
    with open(file_target, 'a') as fw:
        fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

    response += f"Sensitive value '{html_escape(input_param.decode())}' hashed and stored<br/>"

    response += "Hash Test executed"
    return response

def do_something(param):
    a24492 = param
    b24492 = a24492 + " SafeStuff"
    b24492 = b24492[:-5] + "Chars"  # replace "Chars"
    map24492 = {'key24492': b24492}
    c24492 = map24492["key24492"]
    d24492 = c24492[:-1]  # extract most of it
    e24492 = base64.b64decode(base64.b64encode(d24492.encode())).decode()  # base64 encode and decode
    f24492 = e24492.split(" ")[0]

    # Simulating the reflection call
    g24492 = "barbarians_at_the_gate"  # static content
    bar = g24492  # This would typically involve more complex logic

    return bar

def html_escape(text):
    return text.replace("&", "&amp;") \
               .replace("<", "&lt;") \
               .replace(">", "&gt;") \
               .replace('"', "&quot;") \
               .replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

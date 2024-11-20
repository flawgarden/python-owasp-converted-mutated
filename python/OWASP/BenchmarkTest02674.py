
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02674", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest02674", '')

    bar = do_something(param)

    try:
        md = hashlib.md5()
        input_data = b'?' if not bar else bar.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/your/testfiles", "passwordFile.txt")
        
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")
        
        return f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        return f"Problem executing hash - TestCase: {str(e)}"

def do_something(param):
    a73069 = param
    b73069 = a73069 + " SafeStuff"
    b73069 = b73069[:-5] + "Chars"
    map73069 = {"key73069": b73069}
    c73069 = map73069["key73069"]
    d73069 = c73069[:-1]
    e73069 = base64.b64decode(base64.b64encode(d73069.encode())).decode()
    f73069 = e73069.split(" ")[0]

    # Simulating ThingInterface behavior
    g73069 = "barbarians_at_the_gate"
    bar = g73069  # This static value simulates the safe execution

    return bar

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

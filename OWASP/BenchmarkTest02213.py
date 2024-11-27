
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02213", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02213", "")

    bar = do_something(param)

    try:
        md = hashlib.sha1()
        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += "Sensitive value '" + escape_html(input_param.decode('utf-8')) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase with hashlib")
        raise Exception(e)

    response += "Hash Test executed"
    return response

def do_something(param):
    thing = create_thing()
    bar = thing.do_something(param)
    return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Placeholder for actual implementation
    class Thing:
        def do_something(self, param):
            return param
    return Thing()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

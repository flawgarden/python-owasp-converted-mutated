
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-02/BenchmarkTest02118", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.args.get("BenchmarkTest02118", "")
    bar = do_something(param)

    try:
        md = hashlib.new("sha1")
        input_data = bar.encode() if isinstance(bar, str) else bar
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash.")
        raise e


def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar


def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

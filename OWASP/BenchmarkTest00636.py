
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-00/BenchmarkTest00636", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = ""
    param = request.form.get('BenchmarkTest00636', "")
    bar = param

    try:
        md = hashlib.sha1()
        input_data = bar.encode() if isinstance(bar, str) else bytes([ord('?')])
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha1()")
        raise e

    response += "Hash Test hashlib.sha1() executed"
    return response


def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02214", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02214', '')

    bar = do_something(param)

    try:
        md = hashlib.sha512()
        input_data = bar.encode('utf-8')

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print(f"Problem executing hash - TestCase: {str(e)}")
        return "An error occurred during hashing."

def do_something(param):
    bar = html_escape(param)
    return bar

def html_escape(text):
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01650", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_logic(request)

    return benchmark_test_logic(request)

def benchmark_test_logic(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01650="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval}' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param  # No need for URL decoding in Flask as it handles that by default

    bar = Test().do_something(request, param)

    try:
        md = hashlib.sha1()
        input_param = bar.encode('utf-8')

        md.update(input_param)
        result = md.digest()

        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print(f"Problem executing hash - {str(e)}")

    return "Hash Test executed"

class Test:

    def do_something(self, request, param):
        num = 106
        return "This_should_always_happen" if (7 * 18) + num > 200 else param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

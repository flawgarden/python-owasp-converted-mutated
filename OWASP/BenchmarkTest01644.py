
import os
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01644", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01644="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01644' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = unquote(param)

    bar = Test().do_something(request, param)

    file_name = None
    try:
        file_name = os.path.join('testfiles', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return (
                f"The beginning of file: '{file_name}' is:\n\n"
                f"{b.decode(errors='ignore')}"
            )
    except Exception as e:
        return f"Couldn't open file: '{file_name}'. Error: {str(e)}"

class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

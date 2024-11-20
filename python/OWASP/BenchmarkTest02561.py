
import os
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'  # Adjust this as needed

@app.route("/pathtraver-03/BenchmarkTest02561", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02561="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02561' in query string."

    param = query_string[param_loc + len(paramval):]

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = unquote(param)

    bar = do_something(param)

    file_name = os.path.join(TESTFILES_DIR, bar)
    
    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return f"The beginning of file: '{esc_html(file_name)}' is:\n\n{esc_html(b.decode())}"
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return f"Couldn't open file: '{file_name}'"

def do_something(param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def esc_html(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

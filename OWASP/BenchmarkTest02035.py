
import os
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02035", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest02035")

    if headers:
        param = headers[0]  # just grab first element

    param = param  # URLDecode is not necessary in Flask as it decodes automatically

    bar = do_something(param)

    file_name = f"testfiles_dir/{bar}"  # Adjust the path as necessary
    try:
        with open(file_name, 'rb') as file:
            b = file.read(1000)
            response.data = f"The beginning of file: '{escape(file_name)}' is:\n\n"
            response.data += escape(b.decode('utf-8', errors='replace'))
    except Exception as e:
        print(f"Couldn't open InputStream on file: '{file_name}'")
        response.data = f"Problem getting InputStream: {escape(str(e))}"
    
    return response

def do_something(param):
    # Simple ? condition that assigns constant to bar on true condition
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")  # Add more escaping as needed

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

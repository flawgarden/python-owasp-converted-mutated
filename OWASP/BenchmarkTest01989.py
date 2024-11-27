
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01989", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Charset', 'Accept-Encoding', 'Connection']:
            continue

        if request.headers.getlist(name):
            param = name
            break

    bar = do_something(param)

    file_name = None
    try:
        file_name = os.path.join("testfiles", bar)

        with open(file_name, 'w') as fos:
            response.data = f"Now ready to write to file: {html_escape(file_name)}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    return response

def do_something(param):
    num = 106
    return "This should never happen" if (7 * 42) - num > 200 else param

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

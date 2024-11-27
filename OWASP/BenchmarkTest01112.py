
import os
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01112", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    for name in request.headers:
        if name not in common_headers:
            param = name
            break

    bar = Test().do_something(request, param)

    file_name = None
    try:
        file_name = os.path.join(TESTFILES_DIR, bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response.data = (f"The beginning of file: '{html_escape(file_name)}' is:\n\n" +
                             html_escape(b.decode('utf-8', errors='ignore')))
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
    
    return response

class Test:
    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

common_headers = {"Accept", "User-Agent", "Host"}  # Examples of common headers
TESTFILES_DIR = "path/to/testfiles"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

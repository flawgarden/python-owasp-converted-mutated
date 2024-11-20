
from flask import Flask, request, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02207", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.values.get('BenchmarkTest02207', '')

    bar = do_something(param)

    file_name = os.path.join("path/to/testfiles", bar)
    is_file_opened = False

    try:
        with open(file_name, 'rb') as is_file:
            is_file_opened = True
            b = is_file.read(1000)
            response.data = (
                f"The beginning of file: '{escape(file_name)}' is:\n\n" +
                escape(b.decode('utf-8', 'ignore'))
            )
    except Exception as e:
        if is_file_opened:
            is_file.close()
        response.data = (
            "Problem getting InputStream: "
            + escape(str(e))
        )

    return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

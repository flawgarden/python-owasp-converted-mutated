
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02201", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ''

    param = request.args.get('BenchmarkTest02201', '')

    bar = do_something(param)

    file_name = os.path.join('path/to/testfiles/', bar)

    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response += ("The beginning of file: '"
                         + escape_html(file_name)
                         + "' is:\n\n"
                         + escape_html(b.decode('utf-8', errors='ignore')))
    except Exception as e:
        response += ("Couldn't open FileInputStream on file: '" + file_name + "'<br>"
                     + "Problem getting FileInputStream: "
                     + escape_html(str(e)))
    
    return response

def do_something(param):
    bar = ''
    guess = 'ABC'
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = 'bob'
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def escape_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

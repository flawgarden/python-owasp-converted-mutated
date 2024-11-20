
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02665", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "Content-Type: text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest02665", None)

    bar = do_something(param)

    file_name = None
    try:
        file_name = os.path.join('testfiles', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return "The beginning of file: '{}' is:\n\n{}".format(
                escape_html(file_name), escape_html(b.decode('utf-8', errors='ignore'))
            )
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return "Problem getting FileInputStream: {}".format(escape_html(str(e)))

def do_something(param):
    bar = None
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

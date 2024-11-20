
import os
from flask import Flask, request, render_template, send_file

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02113", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02113", "")
    bar = do_something(param)

    file_name = os.path.join('path_to_testfiles_dir', bar)
    try:
        return send_file(file_name, as_attachment=False)
    except Exception as e:
        return f"Couldn't open InputStream on file: '{file_name}'. Problem getting InputStream: {str(e)}"

def do_something(param):
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

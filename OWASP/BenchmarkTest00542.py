
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00542", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00542":
                    param = name
                    flag = False
                    break
        if not flag:
            break

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

    response = app.response_class(status=200, mimetype='text/html')
    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", "b"]
    response.set_data(response.get_data(as_text=True).format(bar, *obj))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

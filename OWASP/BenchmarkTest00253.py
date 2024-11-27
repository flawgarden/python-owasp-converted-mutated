
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00253", methods=['GET', 'POST'])
def benchmark_test_00253():
    if request.method == 'GET':
        return benchmark_test_00253_post()

    return benchmark_test_00253_post()

def benchmark_test_00253_post():
    param = ""
    for name in request.headers:
        if name in ['Host', 'User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding']:
            continue

        param = name
        break

    bar = ""
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

    # Save in session
    request.session['userid'] = bar

    return f"Item: 'userid' with value: '{bar}' saved in session."

if __name__ == '__main__':
    app.run(host='0.0.0.0')

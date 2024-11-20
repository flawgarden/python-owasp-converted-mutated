
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00757", methods=['GET', 'POST'])
def benchmark_test_00757():
    if request.method == 'GET':
        return benchmark_test_00757_post()
    return benchmark_test_00757_post()

def benchmark_test_00757_post():
    values = request.values.getlist('BenchmarkTest00757')
    param = values[0] if values else ""

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

    # Simulate setting session attribute
    request.environ.get('beaker.session')['bar'] = "10340"

    return f"Item: '{bar}' with value: '10340' saved in session."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

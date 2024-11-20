
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02694", methods=['GET', 'POST'])
def benchmark_test_02694():
    response = make_response()
    param = request.args.get("BenchmarkTest02694", "")
    bar = do_something(param)
    
    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    # Simple case statement that assigns param to bar on conditions 'A', 'C', or 'D'
    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session management

@app.route("/trustbound-00/BenchmarkTest00250", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection']:
            continue

        param = name  # Grabs the name of the first non-standard header as the parameter
        break

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

    session[bar] = "10340"

    response.set_data(f"Item: '{bar}' with value: 10340 saved in session.")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

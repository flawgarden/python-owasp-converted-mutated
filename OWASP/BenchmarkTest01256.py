
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01256", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest01256", "")
    
    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = ''.join(bar)  # Convert to string
    return response

class Test:

    def do_something(self, request, param):
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

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

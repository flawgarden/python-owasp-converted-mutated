
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01426", methods=['GET', 'POST'])
def benchmark_test():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    
    param = ""
    flag = True
    names = request.args if request.method == 'GET' else request.form
    for name in names:
        values = names.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01426":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ('C', 'D'):
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

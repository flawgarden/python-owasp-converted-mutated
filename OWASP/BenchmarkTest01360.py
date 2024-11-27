
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01360", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = request.form.get('BenchmarkTest01360', '')

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    try:
        process = os.popen(cmd + bar)
        result = process.read()
        response.set_data(result)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
    
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
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

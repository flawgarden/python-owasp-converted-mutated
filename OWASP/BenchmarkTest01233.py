
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "testfiles"

@app.route("/pathtraver-01/BenchmarkTest01233", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get("BenchmarkTest01233", "")
    bar = Test().do_something(request, param)

    file_target = os.path.join(TESTFILES_DIR, bar)
    response.data = f"Access to file: '{file_target}' created."
    
    if os.path.exists(file_target):
        response.data += " And file already exists."
    else:
        response.data += " But file doesn't exist yet."
    
    return response

class Test:

    def do_something(self, request, param):
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')

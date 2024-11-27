
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01290", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = ''
    param = request.form.get('BenchmarkTest01290', '')

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        process = os.popen(cmd + ' ' + ' '.join(args_env))
        response = process.read()
        process.close()
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = ''
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

def get_insecure_os_command_string():
    # Placeholder for the command retrieval logic
    return "your_command_here"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

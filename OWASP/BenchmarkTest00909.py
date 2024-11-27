
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00909", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.values.get("BenchmarkTest00909")

    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    cmd = "your_command_here"  # Update this to get the insecure command string
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args), 'w')
        print(bar, file=process)
        process.close()
        response.data = "Command executed successfully."
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

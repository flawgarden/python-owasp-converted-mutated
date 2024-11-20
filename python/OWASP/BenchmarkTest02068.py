
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02068", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if 'BenchmarkTest02068' in request.headers:
        param = request.headers['BenchmarkTest02068']  # just grab first element

    param = param.encode('utf-8').decode('utf-8')  # URL decode header value

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args))
        output = process.read()
        response.data = output.encode('utf-8')
    except Exception as e:
        response.data = f"Problem executing cmd - TestCase: {str(e)}".encode('utf-8')
        return response

    return response

def do_something(request, param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

def get_insecure_os_command_string():
    # Placeholder function for the insecure OS command string
    return "insecure_command"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

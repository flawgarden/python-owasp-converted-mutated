
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02344", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    flag = True
    names = request.args.to_dict()
    for name, values in names.items():
        if flag:
            for value in values:
                if value == "BenchmarkTest02344":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_html(str(e))
        return response

    return response

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def get_insecure_os_command_string():
    # Assuming this method is defined in your helper
    return "your_insecure_os_command"

def escape_html(text):
    # Replace special HTML characters to avoid XSS
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

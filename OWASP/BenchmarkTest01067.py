
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01067", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = request.headers.get("BenchmarkTest01067", "")

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {bar}")
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(escape_html(str(e)))
        return response

    return response

class Test:

    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        return bar

def get_insecure_os_command_string():
    return "insecure_command"

def escape_html(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

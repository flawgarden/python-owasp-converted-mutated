
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01920", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.headers.get('Referer', "")

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(f"Formatted like: {bar} and b.")
    return response

def do_something(param):
    bar = ""
    if param:
        valuesList = []
        valuesList.append("safe")
        valuesList.append(param)
        valuesList.append("moresafe")

        valuesList.pop(0)  # remove the 1st safe value

        bar = valuesList[0]  # get the param value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

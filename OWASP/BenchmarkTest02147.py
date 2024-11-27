
import os
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-02/BenchmarkTest02147", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.args.get("BenchmarkTest02147", "")
    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Windows

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return Response(output, content_type='text/html;charset=UTF-8')
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return Response(str(e), content_type='text/html;charset=UTF-8')


def do_something(param):
    return param


if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/xss-00/BenchmarkTest00382", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00382', '')

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.response = '{}, {}'.format(bar, obj)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

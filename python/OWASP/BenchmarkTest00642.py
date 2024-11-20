
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, name):
        return self.request.args.get(name)

@app.route("/xss-01/BenchmarkTest00642", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = make_response()
        scr = SeparateClassRequest(request)
        param = scr.getTheParameter("BenchmarkTest00642")
        if param is None:
            param = ""

        bar = ""
        if param is not None:
            valuesList = ["safe", param, "moresafe"]
            valuesList.pop(0)  # remove the 1st safe value
            bar = valuesList[0]  # get the param value

        response.headers["X-XSS-Protection"] = "0"
        response.data = bar.encode('utf-8')
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

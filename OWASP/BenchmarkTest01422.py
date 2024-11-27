
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01422", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        if flag:
            values = request.args.getlist(name)
            for value in values:
                if value == "BenchmarkTest01422":
                    param = name
                    flag = False

    bar = Test().do_something(param)
    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map_80775 = {}
        map_80775["keyA-80775"] = "a_Value"  # put some stuff in the collection
        map_80775["keyB-80775"] = param      # put it in a collection
        map_80775["keyC"] = "another_Value"   # put some stuff in the collection
        bar = map_80775["keyB-80775"]         # get it back out
        bar = map_80775["keyA-80775"]         # get safe value back out

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

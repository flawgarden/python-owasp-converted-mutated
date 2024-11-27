
from flask import Flask, request
import io

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01439", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01439":
                    param = name
                    flag = False

    bar = Test().do_something(request, param)

    response = io.StringIO()
    response.write(f"Parameter value: {bar}")
    return response.getvalue()

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map95590 = {
            "keyA-95590": "a_Value",
            "keyB-95590": param,
            "keyC": "another_Value"
        }
        bar = map95590["keyB-95590"]
        bar = map95590["keyA-95590"]
        
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

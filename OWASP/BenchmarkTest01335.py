
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01335", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest01335', "")

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", bar]
    response.set_data(f"<!DOCTYPE html>\n<html>\n<body>\n<p>\nFormatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>")
    return response

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map45376 = {}
        map45376["keyA-45376"] = "a-Value"  # put some stuff in the collection
        map45376["keyB-45376"] = param      # put it in a collection
        map45376["keyC"] = "another-Value"   # put some stuff in the collection
        bar = map45376.get("keyB-45376")     # get it back out

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

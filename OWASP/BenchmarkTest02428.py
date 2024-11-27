
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02428", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class(
        content_type='text/html;charset=UTF-8'
    )

    param = request.args.get("BenchmarkTest02428")
    if param is None:
        param = ""

    bar = do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Adjust this based on your specific command for Windows

    try:
        p = os.popen(cmd + bar)
        output = p.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Use proper encoding as needed
        return response

def do_something(request, param):
    bar = "safe!"
    map_52815 = {
        "keyA-52815": "a_Value",
        "keyB-52815": param,
        "keyC": "another_Value"
    }
    bar = map_52815.get("keyB-52815")
    bar = map_52815.get("keyA-52815")

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

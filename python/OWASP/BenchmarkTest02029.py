
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02029", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get('BenchmarkTest02029', '')
    param = os.environ.get(param) if param else param

    bar = do_something(param)

    file_target = os.path.join(bar)
    response_message = f"Access to file: '{file_target}' created."

    exists_message = " And file already exists." if os.path.exists(file_target) else " But file doesn't exist yet."

    return f"{response_message}{exists_message}"

def do_something(param):
    bar = "safe!"
    map_96688 = {
        "keyA-96688": "a_Value",
        "keyB-96688": param,
        "keyC": "another_Value"
    }
    bar = map_96688.get("keyB-96688")
    bar = map_96688.get("keyA-96688")

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

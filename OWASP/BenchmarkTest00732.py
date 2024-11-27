
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00732", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    values = request.values.getlist("BenchmarkTest00732")
    param = values[0] if values else ""

    bar = "safe!"
    map99333 = {
        "keyA-99333": "a_Value",
        "keyB-99333": param,
        "keyC": "another_Value"
    }
    bar = map99333["keyB-99333"]
    bar = map99333["keyA-99333"]

    a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
    args = [a1, a2, f"echo {bar}"]

    try:
        result = os.popen(" ".join(args)).read()
        return result
    except Exception as e:
        print("Problem executing cmdi - subprocess error")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

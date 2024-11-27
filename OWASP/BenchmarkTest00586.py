
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00586", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00586":
                    param = name
                    flag = False
                    break

    bar = "safe!"
    map58886 = {
        "keyA-58886": "a_Value",
        "keyB-58886": param,
        "keyC": "another_Value"
    }

    bar = map58886.get("keyB-58886")
    bar = map58886.get("keyA-58886")

    with app.app_context():
        request.environ['werkzeug.server.shutdown']  # Placeholder for session management
        request.session[bar] = "10340"

    return f"Item: '{bar}' with value: 10340 saved in session."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

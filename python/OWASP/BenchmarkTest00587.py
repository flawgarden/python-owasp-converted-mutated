
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00587", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00587":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "safe!"
    map44465 = {
        "keyA-44465": "a-Value",
        "keyB-44465": param,
        "keyC": "another-Value"
    }
    bar = map44465["keyB-44465"]

    # Flask session usage
    from flask import session
    session[bar] = "10340"

    return f"Item: '{escape(bar)}' with value: '10340' saved in session."

from markupsafe import escape

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

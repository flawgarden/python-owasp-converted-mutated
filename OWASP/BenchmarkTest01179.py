
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01179", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    referer_header = request.headers.get('Referer')

    if referer_header:
        param = referer_header  # just grab first element

    param = os.path.normpath(param)  # URL decode
    bar = Test().do_something(param)

    return bar

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

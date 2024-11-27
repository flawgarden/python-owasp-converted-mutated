
import os
from flask import Flask, request, render_template, abort
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/pathtraver-02/BenchmarkTest01746", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest01746")

    bar = Test().do_something(request, param)

    start_uri_slashes = ""
    if os.name == "nt":
        start_uri_slashes = "/"
    else:
        start_uri_slashes = "//"

    try:
        file_uri = urllib.parse.urljoin(
            "file:",
            start_uri_slashes + os.path.join(
                os.path.abspath('testfiles').replace('\\', '/').replace(' ', '_'),
                bar
            )
        )
        file_target = os.path.abspath(file_uri)

        response_content = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_content += " And file already exists."
        else:
            response_content += " But file doesn't exist yet."

        return render_template("response.html", response=response_content)
    except Exception as e:
        abort(500, str(e))


class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

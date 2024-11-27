
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest01747", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        param = request.form.get("BenchmarkTest01747")

        bar = Test().do_something(request, param)

        start_uri_slashes = ""
        if os.name == "nt":
            start_uri_slashes = "/"
        else:
            start_uri_slashes = "//"

        try:
            file_uri = f"file:{start_uri_slashes}{os.path.join('testfiles', bar.replace(' ', '_'))}"
            file_target = os.path.normpath(file_uri)
            response.set_data(f"Access to file: '{file_target}' created.")
            if os.path.exists(file_target):
                response.set_data(response.get_data(as_text=True) + " And file already exists.")
            else:
                response.set_data(response.get_data(as_text=True) + " But file doesn't exist yet.")
        except Exception as e:
            raise Exception(e)
        return response

class Test:

    def do_something(self, request, param):
        bar = None
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

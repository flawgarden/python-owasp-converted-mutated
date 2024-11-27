
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01748", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == "GET":
        return benchmark_test()
    else:
        param = request.form.get("BenchmarkTest01748", None)
        bar = Test().do_something(param)

        file_name = None
        try:
            file_name = os.path.join("testfiles", bar)
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)

            return "The beginning of file: '{}' is:\n\n{}".format(
                html_escape(file_name),
                html_escape(b.decode('utf-8', errors='replace'))
            )
        except Exception as e:
            return "Problem getting FileInputStream: {}".format(html_escape(str(e)))

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[1]  # get the last 'safe' value

        return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

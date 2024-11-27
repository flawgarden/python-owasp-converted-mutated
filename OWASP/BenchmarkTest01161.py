
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'

@app.route("/pathtraver-01/BenchmarkTest01161", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.headers.get('BenchmarkTest01161', '')

        param = param.encode('utf-8').decode('utf-8')

        bar = Test().do_something(request, param)

        file_name = None
        fos = None

        try:
            file_name = os.path.join(TESTFILES_DIR, bar)
            fos = open(file_name, 'w')
            return f"Now ready to write to file: {escape_html(file_name)}"

        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        finally:
            if fos is not None:
                try:
                    fos.close()
                except Exception:
                    pass

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

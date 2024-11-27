
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01573", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = 'text/html;charset=UTF-8'
    values = request.form.getlist('BenchmarkTest01573')
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    file_name = None
    try:
        file_name = os.path.join('path/to/test/files', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return f"The beginning of file: '{file_name}' is:\n\n{b.decode()}"
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
        return f"Problem getting FileInputStream: {str(e)}"

class Test:
    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = []
            values_list.append("safe")
            values_list.append(param)
            values_list.append("moresafe")

            values_list.pop(0)

            bar = values_list[1]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

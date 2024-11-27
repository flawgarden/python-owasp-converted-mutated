
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01407", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    for name in request.args.keys():
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01407":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    file_name = os.path.join("testfiles", bar)

    try:
        with open(file_name, 'a') as f:  # Append mode to avoid overwriting
            response_text = f"Now ready to write to file: {file_name}"
            return render_template("index.html", content=response_text)
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return render_template("index.html", content=f"Error: {e}")

class Test:
    def do_something(self, param):
        bar = ""

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

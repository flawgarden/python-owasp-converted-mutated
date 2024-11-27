
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01238", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response_type = "text/html;charset=UTF-8"
        param = request.form.get('BenchmarkTest01238', '')

        bar = Test().do_something(param)

        file_name = None
        fos = None

        try:
            file_name = os.path.join('testfiles', bar)

            fos = open(file_name, 'w')
            return f"Now ready to write to file: {file_name}"

        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        finally:
            if fos:
                try:
                    fos.close()
                except Exception:
                    pass

    return render_template("index.html")

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

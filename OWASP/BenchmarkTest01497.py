
from flask import Flask, request, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.remove('safe')
            bar = values_list[0]
        return bar

@app.route("/pathtraver-01/BenchmarkTest01497", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = "text/html;charset=UTF-8"
        param = request.args.get("BenchmarkTest01497", "")
        
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
            if fos is not None:
                try:
                    fos.close()
                except Exception as e:
                    pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

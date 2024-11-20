
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02108", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get("BenchmarkTest02108", "")
        bar = do_something(param)

        file_name = None
        fos = None

        try:
            file_name = os.path.join('testfiles/', bar)

            with open(file_name, 'w') as fos:
                response.data = f"Now ready to write to file: {file_name}"

        except Exception as e:
            print(f"Couldn't open file output stream on file: '{file_name}'")
        finally:
            if fos is not None:
                try:
                    fos.close()
                except Exception as e:
                    pass

        return response

def do_something(param):
    bar = "safe!"
    map44255 = {}
    map44255["keyA-44255"] = "a_Value"
    map44255["keyB-44255"] = param
    map44255["keyC"] = "another_Value"
    bar = map44255["keyB-44255"]
    bar = map44255["keyA-44255"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

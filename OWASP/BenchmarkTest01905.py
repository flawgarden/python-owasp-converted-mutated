
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest01905", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest01905", "")
    param = param.encode().decode('utf-8')

    bar = do_something(request, param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join('testfiles/', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response.set_data("The beginning of file: '{}'\n\n".format(escape(file_name)))
            response.set_data(response.get_data(as_text=True) + escape(b.decode('utf-8')[:len(b)]))
    except Exception as e:
        print("Couldn't open FileInputStream on file: '{}'".format(file_name))
    finally:
        if fis:
            try:
                fis.close()
            except Exception as e:
                pass

    return response

def do_something(request, param):
    bar = "safe!"
    map_33587 = {}
    map_33587["keyA-33587"] = "a_Value"
    map_33587["keyB-33587"] = param
    map_33587["keyC"] = "another_Value"
    bar = map_33587["keyB-33587"]
    bar = map_33587["keyA-33587"]

    return bar

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

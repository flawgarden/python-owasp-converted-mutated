
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00265", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    headers = request.headers.getlist("BenchmarkTest00265")

    if headers:
        param = headers[0]

    param = param

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    file_name = None
    fos = None

    try:
        file_name = os.path.join('testfiles', bar)
        fos = open(file_name, 'w')
        response.data = f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    finally:
        if fos is not None:
            try:
                fos.close()
            except Exception:
                pass

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

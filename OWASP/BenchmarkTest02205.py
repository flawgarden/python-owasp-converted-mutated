
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02205", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    map = request.form.to_dict()
    param = ""
    if map:
        values = map.get("BenchmarkTest02205")
        if values:
            param = values[0]

    bar = do_something(request, param)

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
                fos = None
            except Exception as e:
                pass

def do_something(request, param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

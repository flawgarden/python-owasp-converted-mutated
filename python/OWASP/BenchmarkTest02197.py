
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02197", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = "text/html;charset=UTF-8"
    
    param = ''
    if request.method == 'POST':
        map = request.form
        if map:
            values = map.getlist('BenchmarkTest02197')
            if values:
                param = values[0]

    bar = do_something(request, param)

    file_target = os.path.join('path/to/test/files', bar)
    
    response_text = "Access to file: '{}' created.".format(file_target)
    if os.path.exists(file_target):
        response_text += " And file already exists."
    else:
        response_text += " But file doesn't exist yet."
    
    return response_text

def do_something(request, param):
    bar = "safe!"
    map35951 = {}
    map35951["keyA-35951"] = "a-Value"
    map35951["keyB-35951"] = param
    map35951["keyC"] = "another-Value"
    bar = map35951["keyB-35951"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

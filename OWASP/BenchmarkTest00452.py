
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00452", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    map_params = request.args
    param = ''
    if map_params:
        values = map_params.getlist('BenchmarkTest00452')
        if values:
            param = values[0]

    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    file_target = os.path.join('testfiles', bar)
    response.data = f"Access to file: '{escape(file_target)}' created."

    if os.path.exists(file_target):
        response.data += " And file already exists."
    else:
        response.data += " But file doesn't exist yet."

    return response

def escape(s):
    return ''.join(c if c.isalnum() or c in ['-', '_', '.', '/'] else ' ' for c in s)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

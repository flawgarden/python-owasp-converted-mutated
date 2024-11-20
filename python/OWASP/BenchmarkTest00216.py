
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00216", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection', 'Host', 'Referer', 'Cookie']:
            continue

        param = name
        break

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    file_target = os.path.join(os.getenv('TESTFILES_DIR', ''), bar)
    response.data = b"Access to file: '" + file_target.encode('utf-8') + b"' created."
    if os.path.exists(file_target):
        response.data += b" And file already exists."
    else:
        response.data += b" But file doesn't exist yet."
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

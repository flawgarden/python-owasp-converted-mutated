
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'uploads/'  # Adjust the directory as needed

@app.route("/pathtraver-01/BenchmarkTest01034", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        content_type='text/html;charset=UTF-8'
    )

    param = request.headers.get("BenchmarkTest01034", "")
    param = param.encode('utf-8').decode('utf-8')  # URL decode the header value

    bar = Test().do_something(param)
    
    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)

        with open(file_name, 'w') as fos:
            response.data = f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    return response

class Test:
    def do_something(self, param):
        bar = ''
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

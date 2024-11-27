
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path/to/test/files/'

@app.route("/pathtraver-00/BenchmarkTest00360", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00360', default="", type=str)

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    fileName = None
    try:
        fileName = os.path.join(TESTFILES_DIR, bar)
        with open(fileName, 'rb') as fis:
            b = fis.read(1000)
            return "The beginning of file: '{}' is:\n\n{}".format(
                fileName,
                b.decode(errors='replace')  # handle potential decode errors
            )
    except Exception as e:
        print("Couldn't open FileInputStream on file: '{}'".format(fileName))
        return "Problem getting FileInputStream: {}".format(str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

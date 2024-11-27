
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'

@app.route("/pathtraver-00/BenchmarkTest00627", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get('BenchmarkTest00627', '')

    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)

        fos = open(file_name, 'wb')
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

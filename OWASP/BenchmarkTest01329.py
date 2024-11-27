
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01329", methods=['GET', 'POST'])
def benchmark_test01329():
    if request.method == 'GET':
        return benchmark_test01329_post()

    return benchmark_test01329_post()

def benchmark_test01329_post():
    param = request.args.get('BenchmarkTest01329', '')

    bar = Test().do_something(param)

    start_uri_slashes = ''
    if os.name == 'nt':
        start_uri_slashes = '/'
    else:
        start_uri_slashes = '//'

    try:
        file_uri = urllib.parse.urljoin(
            'file:',
            start_uri_slashes + os.path.join('testfiles', bar.replace(' ', '_'))
        )
        file_target = os.path.normpath(urllib.parse.urlparse(file_uri).path)
        response_text = f"Access to file: '{escape(file_target)}' created."
        if os.path.exists(file_target):
            response_text += " And file already exists."
        else:
            response_text += " But file doesn't exist yet."
        return response_text
    except Exception as e:
        return str(e)

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

def escape(string):
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

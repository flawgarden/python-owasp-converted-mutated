
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00454", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00454', '')

    bar = param
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"

    file_name = None
    content = ''
    
    try:
        file_name = os.path.join('path_to_test_files_directory', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            content = b.decode('utf-8', errors='ignore')
            return f"The beginning of file: '{file_name}' is:\n\n{content}"
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
        return f"Problem getting FileInputStream: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

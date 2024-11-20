
import os
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00365", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.form.get("BenchmarkTest00365", "")
        bar = "safe!"
        map10106 = {
            "keyA-10106": "a_Value",
            "keyB-10106": param,
            "keyC": "another_Value"
        }
        
        bar = map10106["keyB-10106"]
        bar = map10106["keyA-10106"]

        fileName = os.path.join("path/to/testfiles", bar)
        is_ = None

        try:
            with open(fileName, 'rb') as is_:
                b = is_.read(1000)
                response.set_data(f"The beginning of file: '{bar}' is:\n\n")
                response.set_data(response.get_data(as_text=True) + b.decode('utf-8', errors='ignore'))
        
        except Exception as e:
            print(f"Couldn't open InputStream on file: '{fileName}'")
            response.set_data(response.get_data(as_text=True) + f"Problem getting InputStream: {str(e)}")
        
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00456", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    response = ""

    param = request.args.get('BenchmarkTest00456', '')

    bar = "safe!"
    map49381 = {
        "keyA-49381": "a-Value",
        "keyB-49381": param,
        "keyC": "another-Value"
    }
    bar = map49381["keyB-49381"]

    file_name = None
    fis = None

    try:
        file_name = os.path.join('path/to/test/files', bar)  # Adjust the path as necessary
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response += f"The beginning of file: '{html_escape(file_name)}' is:\n\n"
            response += html_escape(b.decode())
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
    finally:
        if fis is not None:
            try:
                fis.close()
            except Exception:
                pass

    return response, {'Content-Type': response_content_type}

def html_escape(text):
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\"", "&quot;")
            .replace("'", "&#x27;"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

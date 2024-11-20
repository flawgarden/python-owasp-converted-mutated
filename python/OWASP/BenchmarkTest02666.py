
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02666", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02666") if request.method == 'GET' else request.form.get("BenchmarkTest02666")

    bar = do_something(param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join("TESTFILES_DIR", bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response = f"The beginning of file: '{escape_html(file_name)}' is:\n\n"
            response += escape_html(b.decode('utf-8', errors='ignore'))
            return response_content, response
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
    finally:
        if fis is not None:
            try:
                fis.close()
            except Exception:
                pass

def do_something(param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

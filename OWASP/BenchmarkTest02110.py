
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02110", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02110", "")
    bar = do_something(param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join("path/to/testfiles", bar)

        fos = open(file_name, 'w')
        return "Now ready to write to file: " + escape_html(file_name)

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos is not None:
            try:
                fos.close()
            except Exception:
                pass

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

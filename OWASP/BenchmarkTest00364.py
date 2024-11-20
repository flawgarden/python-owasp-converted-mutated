
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00364", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00364", "")

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    file_name = None
    fos = None

    try:
        file_name = os.path.join('testfiles', bar)
        fos = open(file_name, 'w')
        return "Now ready to write to file: " + file_name

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    finally:
        if fos:
            try:
                fos.close()
            except Exception:
                pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')

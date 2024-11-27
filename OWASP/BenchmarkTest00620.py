
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00620", methods=['GET', 'POST'])
def benchmark_test00620():
    if request.method == 'GET':
        return benchmark_test00620_post()
    elif request.method == 'POST':
        return benchmark_test00620_post()

def benchmark_test00620_post():
    param = request.args.get("BenchmarkTest00620", "")
    
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    file_target = os.path.join('testfiles', bar)
    response_message = f"Access to file: '{escape(file_target)}' created."

    if os.path.exists(file_target):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."
    
    return response_message

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02168", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    param = request.args.get("BenchmarkTest02168", "")
    bar = do_something(param)

    # Simulating session attribute
    request.environ['werkzeug.session'] = {'userid': bar}

    return "Item: 'userid' with value: '{}' saved in session.".format(encode_for_html(bar))

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;") 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

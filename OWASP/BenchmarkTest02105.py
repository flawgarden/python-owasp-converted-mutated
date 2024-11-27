
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02105", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = ""
    param = request.args.get("BenchmarkTest02105", "")
    bar = do_something(request, param)

    file_target = os.path.join("testfiles", bar)
    response += f"Access to file: '{escape_html(file_target)}' created.<br>"
    if os.path.exists(file_target):
        response += " And file already exists.<br>"
    else:
        response += " But file doesn't exist yet.<br>"
    return response

def do_something(request, param):
    bar = ""
    if param:
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

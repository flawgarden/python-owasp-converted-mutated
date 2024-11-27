
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01745", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01745")
        bar = do_something(param)

        file_target = os.path.join(bar, "Test.txt")
        response_text = f"Access to file: '{html_escape(file_target)}' created."
        file_exists_text = " And file already exists." if os.path.exists(file_target) else " But file doesn't exist yet."

        return render_template("index.html", response=response_text + file_exists_text)
    return render_template("index.html")

def do_something(param):
    return param

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

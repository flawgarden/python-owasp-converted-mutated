
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01300", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01300", "")
        bar = Test().do_something(request, param)

        # Simulating session storage with a dictionary
        request.session = {}
        request.session['userid'] = bar

        return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def encode_for_html(value):
    # Simple HTML encoding function
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01549", methods=['GET', 'POST'])
def benchmark_test_01549():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get("BenchmarkTest01549")
        if param is None:
            param = ""

        bar = Test().do_something(request, param)

        # Save item in session
        request.environ.get('werkzeug.session').set('userid', bar)

        return "Item: 'userid' with value: '{}' saved in session.".format(escape_html(bar))

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        return bar

def escape_html(data):
    return str(data).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

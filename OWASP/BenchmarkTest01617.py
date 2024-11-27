
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01617", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class(content_type='text/html;charset=UTF-8')

        values = request.form.getlist('BenchmarkTest01617')
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        # setting session attribute
        request.environ['werkzeug.server.shutdown'] = bar, "10340"

        response.data = (
            "Item: '"
            + Utils.encode_for_html(bar)
            + "' with value: '10340' saved in session."
        ).encode('utf-8')

        return response

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

class Utils:
    @staticmethod
    def encode_for_html(value):
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

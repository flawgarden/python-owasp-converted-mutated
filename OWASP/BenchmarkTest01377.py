
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01377", methods=['GET', 'POST'])
def benchmark_test_01377():
    if request.method == 'GET':
        return benchmark_test_01377_post()
    return benchmark_test_01377_post()

def benchmark_test_01377_post():
    param = request.args.get('BenchmarkTest01377', '')

    bar = Test().do_something(request, param)

    request.session['userid'] = bar

    return "Item: 'userid' with value: '{}' saved in session.".format(encode_for_html(bar))

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def encode_for_html(value):
    import html
    return html.escape(value)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

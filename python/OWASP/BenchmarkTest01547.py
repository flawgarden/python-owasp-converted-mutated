
from flask import Flask, request, session, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required for session management

@app.route("/trustbound-00/BenchmarkTest01547", methods=['GET', 'POST'])
def benchmark_test_01547():
    if request.method == 'GET':
        return benchmark_test_01547()
    else:
        response = app.response_class()
        param = request.values.get("BenchmarkTest01547", "")
        
        bar = Test().do_something(request, param)

        session['userid'] = bar

        response.data = f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."
        response.content_type = "text/html;charset=UTF-8"
        return response

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar

def encode_for_html(value):
    return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

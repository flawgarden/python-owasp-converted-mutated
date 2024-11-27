
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02526", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.form.getlist("BenchmarkTest02526")
    param = values[0] if values else ""

    bar = do_something(request, param)

    # Storing the value in session
    request.session['userid'] = bar

    response.data = f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."
    return response

def do_something(request, param):
    bar = html_escape(param)
    return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

def encode_for_html(text):
    return html_escape(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

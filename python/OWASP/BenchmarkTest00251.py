
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00251", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    names = request.headers.keys()
    
    for name in names:
        if name not in common_headers:
            param = name
            break
    
    bar = ""
    if param:
        bar = param.split(" ")[0]
    
    request.environ['werkzeug.session'].setdefault('userid', bar)

    response.set_data(
        "Item: 'userid' with value: '"
        + encode_for_html(bar)
        + "' saved in session."
    )
    return response

common_headers = set(["Accept", "Accept-Encoding", "User-Agent", "Host", "Connection"])
    
def encode_for_html(value):
    from html import escape
    return escape(value)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

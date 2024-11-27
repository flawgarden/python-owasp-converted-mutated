
from flask import Flask, request, render_template, session
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Change this to a secure random key

@app.route("/trustbound-01/BenchmarkTest02015", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name not in common_headers():
            param = name
            break

    bar = do_something(param)

    session[bar] = "10340"

    return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def encode_for_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def common_headers():
    return set(["Accept", "Accept-Charset", "Accept-Encoding", "Accept-Language", "Authorization", 
                "Cache-Control", "Connection", "Content-Length", "Content-Type", "Cookie", 
                "Host", "If-Modified-Since", "If-None-Match", "Pragma", "User-Agent", 
                "Upgrade-Insecure-Requests"])

if __name__ == "__main__":
    app.run(host='0.0.0.0')

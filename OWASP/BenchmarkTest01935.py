
import os
import urllib.parse
from flask import Flask, request, make_response, render_template
from base64 import b64encode, b64decode
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01935", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01935", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = make_response(render_template("index.html"))
    
    cookie = f'SomeCookie={bar}; Path={request.path}; Secure; HttpOnly'
    response.set_cookie('SomeCookie', bar, secure=True, httponly=True, path=request.path)

    response.data += f"Created cookie: 'SomeCookie': with value: '{escape_html(bar)}' and secure flag set to: true".encode('utf-8')
    return response

def do_something(param):
    a17785 = param
    b17785 = f"{a17785} SafeStuff"
    b17785 = b17785[:-5] + "Chars"
    
    map17785 = {'key17785': b17785}
    c17785 = map17785['key17785']
    d17785 = c17785[:-1]
    e17785 = b64decode(b64encode(d17785.encode('utf-8'))).decode('utf-8')
    f17785 = e17785.split(" ")[0]
    
    thing = create_thing()
    bar = thing.do_something(f17785)

    return bar

class Thing:
    def do_something(self, input):
        return hashlib.md5(input.encode()).hexdigest()

def create_thing():
    return Thing()

def escape_html(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest01833", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("pathtraver-02/BenchmarkTest01833.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest01833=FileName; Max-Age=180; Secure; Path=" + request.path + "; Domain=" + request.host)
        resp.headers.add('Set-Cookie', user_cookie.headers['Set-Cookie'])
        return resp

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01833' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest01833'])

        bar = do_something(request, param)

        file_target = os.path.join('testfiles', bar)
        response_text = "Access to file: '" + escape_html(file_target) + "' created."
        
        if os.path.exists(file_target):
            response_text += " And file already exists."
        else:
            response_text += " But file doesn't exist yet."
        
        return response_text

def do_something(request, param):
    bar = "safe!"
    map9325 = {}
    map9325['keyA-9325'] = "a-Value"
    map9325['keyB-9325'] = param
    map9325['keyC'] = "another-Value"
    bar = map9325['keyB-9325']
    
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

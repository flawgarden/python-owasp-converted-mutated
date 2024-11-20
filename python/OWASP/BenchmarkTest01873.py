
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01873", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("trustbound-01/BenchmarkTest01873.html"))
        user_cookie = make_response("Cookie")
        user_cookie.set_cookie("BenchmarkTest01873", "my_user_id", max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.headers.add('Set-Cookie', user_cookie.cookies)
        return response
    
    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        
        if 'BenchmarkTest01873' in cookies:
            param = cookies['BenchmarkTest01873']
        
        bar = do_something(param)
        request.session['userid'] = bar
        
        return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

def do_something(param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        del values_list[0]  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def encode_for_html(value):
    safe_value = value.replace("<", "&lt;").replace(">", "&gt;")
    return safe_value

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

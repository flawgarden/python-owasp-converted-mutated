
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02622", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02622="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02622' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    bar = do_something(param)

    # Simulating session storage
    request.session[bar] = "10340"

    return "Item: '{}' with value: '10340' saved in session.".format(encode_for_html(bar))

def do_something(param):
    sbxyz66849 = str(param)
    bar = sbxyz66849 + "_SafeStuff"
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

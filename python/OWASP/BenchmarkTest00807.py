
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00807", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_text = ''
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00807="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response_text = ("getQueryString() couldn't find expected parameter '"
                         "BenchmarkTest00807"
                         "' in query string.")
        return response_text

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    bar = ""
    if param:
        bar = param.split(" ")[0]

    response_text = f"<html><body><h1>{bar}</h1></body></html>"
    return response_text

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import base64
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00802", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00802="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = base64.b64decode(param).decode('utf-8') if param else ""

    bar = base64.b64encode(param.encode()).decode() if param else ""
    
    response.headers['X-XSS-Protection'] = "0"
    response.data = bar
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

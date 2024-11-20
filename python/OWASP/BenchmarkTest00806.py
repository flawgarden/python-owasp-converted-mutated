
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00806", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00806="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00806' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = param.replace('%20', ' ')  # Basic URL decoding

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the 1st safe value

        bar = values_list[0]  # get the param value

    response.headers['X-XSS-Protection'] = '0'
    obj = ("a", "b")
    response.data = f"{bar} {obj[0]} {obj[1]}"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

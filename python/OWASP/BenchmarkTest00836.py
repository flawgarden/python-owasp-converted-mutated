
from flask import Flask, request, session, Response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required to use sessions

@app.route("/trustbound-00/BenchmarkTest00836", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    if request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00836="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return Response("getQueryString() couldn't find expected parameter 'BenchmarkTest00836' in query string.", status=400)

    param = query_string[param_loc + len(paramval):]  # Assuming it is the last parameter
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = unquote(param)

    bar = ""
    if param:
        bar = param.split(" ")[0]

    session['userid'] = bar

    return Response("Item: 'userid' with value: '{}' saved in session.".format(bar), content_type="text/html;charset=UTF-8")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00891", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.args.get("BenchmarkTest00891", "")
    
    bar = ""
    guess = "ABC"
    switchTarget = guess[1]  # condition 'B', which is safe

    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bob"
    elif switchTarget in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"
    
    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar:
        length = len(bar)
        response.response = bar[:length]

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

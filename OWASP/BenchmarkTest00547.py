
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00547", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00547":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = ""
    if param:
        bar = param.split(" ")[0]

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(bar % obj)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

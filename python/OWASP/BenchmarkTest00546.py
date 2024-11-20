
from flask import Flask, request, Response


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00546", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00546":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

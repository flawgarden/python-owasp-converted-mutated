
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00551", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = make_response()
        response.content_type = "text/html;charset=UTF-8"

        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            values = request.values.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest00551":
                        param = name
                        flag = False
                        break
            if not flag:
                break

        bar = param

        response.headers["X-XSS-Protection"] = "0"
        response.data = bar
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

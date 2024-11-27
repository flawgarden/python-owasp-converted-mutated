
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00646", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest00646")
    if param is None:
        param = ""

    bar = "alsosafe"
    if param:
        valuesList = []
        valuesList.append("safe")
        valuesList.append(param)
        valuesList.append("moresafe")

        valuesList.pop(0)  # Remove the 1st safe value

        bar = valuesList[1]  # Get the last 'safe' value

    response.headers["X-XSS-Protection"] = "0"
    response.data = bar.encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

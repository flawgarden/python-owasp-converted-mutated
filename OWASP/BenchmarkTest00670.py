
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/trustbound-00/BenchmarkTest00670", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()

    param = request.form.get("BenchmarkTest00670", "")

    bar = param
    if param and len(param) > 1:
        sbxyz42704 = list(param)
        sbxyz42704[-1] = 'Z'
        bar = ''.join(sbxyz42704)

    request.environ['werkzeug.session'].set(bar, "10340")

    response.response = [
        f"Item: '{bar}' with value: 10340 saved in session."
    ]
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

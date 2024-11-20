
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00493", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    values = request.args.getlist('BenchmarkTest00493')
    if values:
        param = values[0]

    bar = "safe!"
    map8943 = {
        "keyA-8943": "a_Value",  # put some stuff in the collection
        "keyB-8943": param,      # put it in a collection
        "keyC": "another_Value"   # put some stuff in the collection
    }
    bar = map8943.get("keyB-8943")  # get it back out
    bar = map8943.get("keyA-8943")  # get safe value back out

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(f"Parameter value: {bar}")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00886", methods=['GET', 'POST'])
def benchmark_test_00886():
    if request.method == 'GET':
        return benchmark_test_00886_post()
    return benchmark_test_00886_post()

def benchmark_test_00886_post():
    param = request.args.get('BenchmarkTest00886', '')
    bar = "safe!"
    map8361 = {
        "keyA-8361": "a_Value",
        "keyB-8361": param,
        "keyC": "another_Value"
    }
    bar = map8361.get("keyB-8361")
    bar = map8361.get("keyA-8361")

    response = app.response_class(
        response=f"Formatted like: {bar} and b.",
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import base64
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00478", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.values.get('BenchmarkTest00478', '')

    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found', 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')

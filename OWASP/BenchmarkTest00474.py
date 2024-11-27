
from flask import Flask, request, Response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00474", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.args.get('BenchmarkTest00474', '')
    bar = html.escape(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')

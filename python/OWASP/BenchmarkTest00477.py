
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00477", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )
    
    param = request.args.get('BenchmarkTest00477', '')
    
    sbxyz54686 = str(param)
    bar = sbxyz54686 + "_SafeStuff"
    
    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

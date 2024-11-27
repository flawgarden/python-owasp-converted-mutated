
import os
from flask import Flask, request, render_template
import urllib.parse
from html import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00285", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ''
        referer_header = request.headers.get('Referer')
        
        if referer_header:
            param = referer_header
        
        param = urllib.parse.unquote(param)
        bar = escape(param)

        response = app.response_class()
        response.headers['X-XSS-Protection'] = '0'
        response.data = bar
        response.mimetype = 'text/html'
        return response
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

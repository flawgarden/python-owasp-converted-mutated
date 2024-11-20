
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-01/BenchmarkTest00718", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00718")
    param = values[0] if values else ""
    bar = escape_html(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.set_data("Formatted like: %s and %s." % (obj[0], obj[1]))
    return response


def escape_html(s):
    return (s.replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;")
               .replace('"', "&quot;")
               .replace("'", "&apos;"))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

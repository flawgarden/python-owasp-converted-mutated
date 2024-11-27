
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-00/BenchmarkTest00149", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")

    param = request.headers.get("Referer", "")

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    sbxyz19132 = f"{param}"
    bar = f"{sbxyz19132}_SafeStuff"

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(f"Formatted like: a and {bar}.")

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')

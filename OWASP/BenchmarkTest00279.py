
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00279", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        param = ""
        headers = request.headers.getlist("Referer")

        if headers:
            param = headers[0]  # just grab the first element

        # URL Decode the header value
        param = urllib.parse.unquote(param)

        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value

            if values_list:
                bar = values_list[0]  # get the param value

        response = app.response_class()
        response.headers["X-XSS-Protection"] = "0"
        response.set_data(bar)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

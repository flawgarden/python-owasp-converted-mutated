
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00377", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00377", "")
    
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    response = app.response_class()
    response.headers["X-XSS-Protection"] = "0"
    response.data = f"Formatted like: a and {bar}."
    response.content_type = "text/html;charset=UTF-8"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

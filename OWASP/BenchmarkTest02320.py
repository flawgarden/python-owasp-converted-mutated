
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-04/BenchmarkTest02320", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return do_post(request)


def do_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    flag = True
    names = request.args

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02320":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"Formatted like: a and {bar}."
    return response


def do_something(param):
    from html import escape
    bar = escape(param)
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

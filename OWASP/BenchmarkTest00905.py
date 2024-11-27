
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00905", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.form.get('BenchmarkTest00905')
    bar = param

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    osName = os.name

    if osName == 'nt':  # Windows
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo"
        args = [a1, a2, cmd + " " + bar]
    else:  # POSIX (Linux, MacOS, etc.)
        a1 = "sh"
        a2 = "-c"
        cmd = "ping -c 1 "
        args = [a1, a2, cmd + bar]

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data("<html>" + str(e) + "</html>")
        return response

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

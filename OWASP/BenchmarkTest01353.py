
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-01/BenchmarkTest01353", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.values.get('BenchmarkTest01353', '')

        bar = Test().do_something(request, param)

        arg_list = []

        os_name = os.name
        if os_name == 'nt':
            arg_list.append('cmd.exe')
            arg_list.append('/c')
        else:
            arg_list.append('sh')
            arg_list.append('-c')
        arg_list.append('echo ' + bar)

        pb = os.popen(' '.join(arg_list))
        output = pb.read()
        pb.close()
        return render_template("index.html", output=output)
    return render_template("index.html")


class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target == 'C' or switch_target == 'D':
            bar = param
        else:
            bar = "bob's your uncle"

        return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

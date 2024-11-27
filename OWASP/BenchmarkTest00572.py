
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00572", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = render_template("index.html")

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00572":
                    param = name
                    flag = False
                    break

    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = ["Foo=bar"]
    try:
        p = os.popen(cmd + bar)
        output = p.read()
        p.close()
        return response + "<pre>" + output + "</pre>"
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return response + "<p>Error: " + str(e) + "</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

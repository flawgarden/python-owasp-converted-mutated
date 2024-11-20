
import os
from flask import Flask, request, render_template
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00559", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    if request.method == 'POST':
        param = ""
        flag = True
        for name in request.args:
            values = request.args.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest00559":
                        param = name
                        flag = False
                        break
            if not flag:
                break

        a39502 = param
        b39502 = str(a39502)
        b39502 += " SafeStuff"
        b39502 = b39502[:-5] + "Chars"
        map39502 = {}
        map39502["key39502"] = b39502
        c39502 = map39502["key39502"]
        d39502 = c39502[:-1]
        e39502 = b64decode(b64encode(d39502.encode())).decode()
        f39502 = e39502.split(" ")[0]

        # Simulating the ThingInterface and ThingFactory
        class ThingInterface:
            def doSomething(self, input_string):
                return "result_from_" + input_string

        thing = ThingInterface()
        g39502 = "barbarians_at_the_gate"
        bar = thing.doSomething(g39502)

        arg_list = []
        os_name = os.name
        if os_name == 'nt':
            arg_list.append("cmd.exe")
            arg_list.append("/c")
        else:
            arg_list.append("sh")
            arg_list.append("-c")
        arg_list.append("echo " + bar)

        try:
            process = os.popen(' '.join(arg_list))
            result = process.read()
            return result
        except Exception as e:
            print("Problem executing cmdi - subprocess start error")
            return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01445", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ""
        flag = True
        names = request.args
        for name in names:
            values = request.args.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest01445":
                        param = name
                        flag = False
                        break
            if not flag:
                break

        bar = Test().do_something(request, param)

        cmd = Utils.get_insecure_os_command_string()

        args_env = [bar]
        try:
            process = os.popen(f"{cmd} {' '.join(args_env)}")
            output = process.read()
            return output
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return str(e)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map3083 = {}
        map3083["keyA-3083"] = "a_Value"
        map3083["keyB-3083"] = param
        map3083["keyC"] = "another_Value"
        bar = map3083["keyB-3083"]
        bar = map3083["keyA-3083"]
        return bar

class Utils:

    @staticmethod
    def get_insecure_os_command_string():
        return "your_command_here"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/cmdi-00/BenchmarkTest00411", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.args.get("BenchmarkTest00411", "")

    a18204 = param
    b18204 = str(a18204) + " SafeStuff"

    b18204 = b18204[:-5] + "Chars"

    map18204 = {}
    map18204["key18204"] = b18204
    c18204 = map18204["key18204"]
    d18204 = c18204[:-1]

    e18204 = d18204.encode('utf-8')
    f18204 = e18204.decode('utf-8').split(" ")[0]

    # Assuming 'thing' is created and used similarly as in Java code
    thing = create_thing()

    g18204 = "barbarians_at_the_gate"
    bar = thing.do_something(g18204)

    cmd = get_insecure_os_command_string()

    args_env = [bar]

    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        results = process.read()
        return results  # Return or render results as needed
    except Exception as e:
        return str(e)


def create_thing():
    # Placeholder for actual implementation
    class ThingInterface:
        def do_something(self, input):
            return input  # Simulate reflection behavior

    return ThingInterface()


def get_insecure_os_command_string():
    # Placeholder for actual implementation
    return "echo"  # Example command


if __name__ == "__main__":
    app.run(host='0.0.0.0')

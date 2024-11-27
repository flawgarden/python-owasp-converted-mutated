
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/pathtraver-01/BenchmarkTest01114", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = ""
    header_names = request.headers.keys()
    for name in header_names:
        if name not in common_headers():
            param = name
            break

    bar = Test().do_something(request, param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)

        with open(file_name, 'w') as fos:
            fos.write(f"Now ready to write to file: {escape_html(file_name)}")

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    return response


class Test:

    def do_something(self, request, param):
        a97099 = param
        b97099 = list(a97099)
        b97099.extend(" SafeStuff")
        b97099 = ''.join(b97099)
        b97099 = b97099[:-5] + "Chars"

        map97099 = {'key97099': b97099}
        c97099 = map97099['key97099']
        d97099 = c97099[:-1]
        e97099 = base64.b64decode(base64.b64encode(d97099.encode())).decode()

        f97099 = e97099.split(" ")[0]
        thing = create_thing()
        g97099 = "barbarians_at_the_gate"
        bar = thing.do_something(g97099)

        return bar


def common_headers():
    return ['Accept', 'Content-Type', 'User-Agent']

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Mockup for the factory method
    return Thing()

class Thing:
    def do_something(self, input):
        return input[::-1]  # Just a placeholder action

TESTFILES_DIR = '/path/to/testfiles'

if __name__ == "__main__":
    app.run(host='0.0.0.0')

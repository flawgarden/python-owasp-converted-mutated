
import os
from flask import Flask, request, render_template
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00220", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers.set('Content-Type', 'text/html;charset=UTF-8')

    param = ""
    for name in request.headers:
        if name in ['Host', 'User-Agent', 'Accept']:
            continue

        param = name
        break

    a25969 = param
    b25969 = str(a25969) + " SafeStuff"
    b25969 = b25969[:-len("Chars")] + "Chars"
    map25969 = {"key25969": b25969}
    c25969 = map25969["key25969"]
    d25969 = c25969[:-1]
    e25969 = b64decode(b64encode(d25969.encode())).decode()
    f25969 = e25969.split(" ")[0]
    thing = create_thing()
    g25969 = "barbarians_at_the_gate"
    bar = thing.do_something(g25969)

    file_name = None
    fos = None

    try:
        file_name = os.path.join('path/to/testfiles/', bar)

        fos = open(file_name, 'w')
        response.data = f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos is not None:
            try:
                fos.close()
            except Exception:
                pass

    return response

def create_thing():
    class Thing:
        def do_something(self, input_value):
            return input_value

    return Thing()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, session, render_template
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'supersecretkey'


@app.route("/trustbound-00/BenchmarkTest01458", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01458":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    session[bar] = '10340'

    return f"Item: '{encode_for_html(bar)}' with value: '10340' saved in session."


class Test:

    def do_something(self, request, param):
        a34936 = param
        b34936 = list(a34936)  # stick it in a list (similar to StringBuilder)
        b34936.append(" SafeStuff")
        b34936 = ''.join(b34936[:-len("Chars")] + ["Chars"])  # replace some of the end content
        map34936 = {}
        map34936["key34936"] = b34936  # put in a collection
        c34936 = map34936["key34936"]  # get it back out
        d34936 = c34936[:-1]  # extract most of it
        e34936 = b64decode(b64encode(d34936.encode())).decode()  # B64 encode and decode it
        f34936 = e34936.split(" ")[0]  # split it on a space
        bar = create_thing().do_something(f34936)  # reflection

        return bar


def encode_for_html(input_string):
    return input_string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Assuming Thing is a class you want to simulate. Implement as needed.
    class Thing:
        def do_something(self, value):
            return value  # Placeholder for the actual implementation

    return Thing()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

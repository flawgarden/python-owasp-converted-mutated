
from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02380", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return do_post(request)

def do_post(request):
    response = request.response
    response.content_type = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02380", "")
    bar = do_something(param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join("testfiles_dir", bar)

        with open(file_name, 'wb') as fos:
            response.data = f"Now ready to write to file: {escape_html(file_name)}".encode('utf-8')

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos is not None:
            try:
                fos.close()
                fos = None
            except Exception as e:
                pass

def do_something(param):
    a76789 = param
    b76789 = f"{a76789} SafeStuff"
    b76789 = b76789[:-5] + "Chars"
    map76789 = {"key76789": b76789}
    c76789 = map76789["key76789"]
    d76789 = c76789[:-1]
    e76789 = base64.b64decode(base64.b64encode(d76789.encode('utf-8'))).decode('utf-8')
    f76789 = e76789.split(" ")[0]
    thing = create_thing()
    g76789 = "barbarians_at_the_gate"
    bar = thing.do_something(g76789)
    return bar

class ThingInterface:
    def do_something(self, value):
        return value

def create_thing():
    return ThingInterface()

def escape_html(text):
    return ''.join(
        {
            '<': '&lt;',
            '>': '&gt;',
            '&': '&amp;',
            '"': '&quot;',
            "'": '&#39;'
        }.get(c, c) for c in text
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

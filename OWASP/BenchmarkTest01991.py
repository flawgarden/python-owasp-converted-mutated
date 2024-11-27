
import os
from flask import Flask, request, render_template, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01991", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    param = ""
    
    for name in request.headers:
        if name in ['Content-Type', 'Accept', 'User-Agent']:  # Common headers
            continue
        param = name
        break
    
    bar = do_something(request, param)

    file_name = os.path.join('testfiles', bar)
    
    try:
        with open(file_name, 'rb') as is_file:
            b = is_file.read(1000)
            response.set_data("The beginning of file: '"
                              + escape_html(file_name) + "' is:\n\n"
                              + escape_html(b.decode()))
    except Exception as e:
        print("Couldn't open InputStream on file: '" + file_name + "'")
        response.set_data("Problem getting InputStream: " + escape_html(str(e)))
    
    return response

def do_something(request, param):
    a81108 = param
    b81108 = list(a81108)
    b81108.append(" SafeStuff")
    b81108 = ''.join(b81108)
    b81108 = b81108[:-len("Chars")] + "Chars"
    map81108 = {}
    map81108["key81108"] = b81108
    c81108 = map81108["key81108"]
    d81108 = c81108[:-1]
    e81108 = base64.b64decode(base64.b64encode(d81108.encode())).decode()
    f81108 = e81108.split(" ")[0]

    # Simulate a call to wrapped functionality
    g81108 = "barbarians_at_the_gate"
    bar = do_safe_action(g81108)

    return bar

def do_safe_action(input_str):
    return input_str  # This simulates the safe action

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

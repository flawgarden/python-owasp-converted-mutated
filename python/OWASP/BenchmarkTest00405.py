
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00405", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest00405", "")
    
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    str_value = param if param else "No cookie value supplied"
    cookie = str_value

    response.set_cookie("SomeCookie", cookie, secure=True, httponly=True, path=request.path)
    
    encoded_str = escape(str_value)
    response.data = f"Created cookie: 'SomeCookie': with value: '{encoded_str}' and secure flag set to: true"
    return response

def escape(input_string):
    return input_string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/crypto-01/BenchmarkTest00943", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("crypto-01/BenchmarkTest00943.html"))
        user_cookie = ('BenchmarkTest00943', 'someSecret')
        resp.set_cookie(user_cookie[0], user_cookie[1], max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00943' in the_cookies:
            param = the_cookies['BenchmarkTest00943']

        bar = Test().do_something(request, param)

        try:
            cipher = get_cipher()
            input_data = b'?'  # Example input
            if isinstance(bar, str):
                input_data = bar.encode()

            result = cipher.do_final(input_data)

            file_target = os.path.join('path/to/your/testfiles_dir', 'passwordFile.txt')
            with open(file_target, 'a') as fw:
                fw.write("secret_value=" + base64.b64encode(result).decode('utf-8') + "\n")

            return f"Sensitive value: '{html_encode(input_data.decode())}' encrypted and stored<br/>"

        except Exception as e:
            return f"Problem executing crypto - {str(e)}", 500

    return "Invalid request", 400

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # Remove the 1st safe value
            bar = values_list[0]  # Get the param value
        return bar

def get_cipher():
    # Your implementation for getting the cipher should go here
    pass

def html_encode(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;").replace('"', "&quot;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

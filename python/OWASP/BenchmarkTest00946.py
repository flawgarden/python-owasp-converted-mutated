
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/crypto-01/BenchmarkTest00946", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("crypto-01/BenchmarkTest00946.html"))
        user_cookie = ('BenchmarkTest00946', 'someSecret', 60*3, True)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3])
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00946' in cookies:
            param = cookies['BenchmarkTest00946']

        bar = Test().do_something(request, param)

        try:
            algorithm = "DES"  # Placeholder for the algorithm, adjust based on your needs
            # Placeholder: implement your encryption logic here.
            # Example: `cipher = DES.new(key, DES.MODE_ECB)`
            
            input_data = bytes(b'?')
            if isinstance(bar, bytes):
                input_data = bar
            else:
                input_data = bar.encode()

            # Here you'd perform encryption (not implemented)
            # result = cipher.encrypt(input_data)

            result = base64.b64encode(input_data).decode('utf-8')

            with open(os.path.join('testfiles', "passwordFile.txt"), 'a') as fw:
                fw.write("secret_value=" + result + "\n")

            return f"Sensitive value: '{base64.b64encode(input_data).decode()}' encrypted and stored<br/>"

        except Exception as e:
            return f"Problem executing crypto - {str(e)}"

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

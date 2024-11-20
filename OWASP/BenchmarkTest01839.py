
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote


app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest01839", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-02/BenchmarkTest01839.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01839", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(':')[0])
        response.set_cookie(user_cookie)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if 'BenchmarkTest01839' in cookies:
            param = unquote(cookies['BenchmarkTest01839'])

        bar = do_something(request, param)

        file_name = None
        fos = None

        try:
            file_name = os.path.join('testfiles/', bar)

            with open(file_name, 'w') as fos:
                return f"Now ready to write to file: {file_name}"

        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        finally:
            if fos:
                fos.close()

def do_something(request, param):
    # Simple condition that assigns param to bar on false condition
    num = 106
    bar = param if (7 * 42) - num <= 200 else "This should never happen"
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

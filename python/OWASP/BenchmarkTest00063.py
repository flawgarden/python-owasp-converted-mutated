
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00063", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00063.html"))
        user_cookie = ('BenchmarkTest00063', 'FileName', 60 * 3)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00063' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00063'])

        bar = None
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

        file_name = None
        try:
            file_name = os.path.join('testfiles', bar)
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                response_text = f"The beginning of file: '{file_name}' is:\n\n{b.decode()}"
                return render_template('result.html', response_text=response_text)
        except Exception as e:
            print(f"Couldn't open FileInputStream on file: '{file_name}'")
            return render_template('error.html', error_message=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

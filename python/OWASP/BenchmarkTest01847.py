
import os
import hashlib
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01847", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-02/BenchmarkTest01847.html"))
        user_cookie = ('BenchmarkTest01847', 'someSecret', 60 * 3)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host.split(':')[0])
        return response
    
    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest01847' in the_cookies:
            param = the_cookies['BenchmarkTest01847']

        bar = do_something(param)

        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode('utf-8')

        md = hashlib.new('sha384')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path/to/testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>" \
               f"Hash Test executed"

def do_something(param):
    bar = ""
    if param:
        values_list = ['safe', param, 'moresafe']
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

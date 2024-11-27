
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00346", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post()
    else:
        return do_post()

def do_post():
    input_stream = request.stream
    content_type = request.content_type

    if content_type != 'application/octet-stream':
        return "This input source requires a POST with an appropriate content type."

    input_data = input_stream.read(1000) or b'\x3f'  # Default to '?' if no data

    import hashlib
    hash_object = hashlib.new('sha1')
    hash_object.update(input_data)

    result = hash_object.digest()
    file_target = os.path.join('testfiles', 'passwordFile.txt')

    with open(file_target, 'a') as fw:
        fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

    return "Sensitive value '{}' hashed and stored<br/>".format(base64.b64encode(input_data).decode('utf-8'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

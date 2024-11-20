
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00641", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    bar = ""
    param = request.args.get("BenchmarkTest00641", "")

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        algorithm = "SHA256"  # default algorithm
        # Load properties would typically involve reading from a file.
        # For simplicity, it is hardcoded here.
        hash_alg = os.getenv("HASH_ALG", algorithm)  # Example use of environment variable for the algorithm
        md = hashlib.new(hash_alg)

        input_param = bar.encode()  # Assume bar is string
        md.update(input_param)

        result = md.digest()
        target_file = os.path.join('uploads', "passwordFile.txt")

        with open(target_file, 'ab') as fw:  # Append mode
            fw.write(b"hash_value=" + result + b"\n")

        response_msg = f"Sensitive value '{param}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        return "An error occurred", 500

    return response_msg + "Hash Test executed"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

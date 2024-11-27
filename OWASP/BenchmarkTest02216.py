
import os
import hashlib
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = './testfiles'  # Adjust path as necessary

@app.route("/hash-02/BenchmarkTest02216", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.values.get("BenchmarkTest02216", "")

    bar = do_something(param)

    try:
        md = hashlib.new("sha512")
        input_data = bar.encode() if isinstance(bar, str) else bytes(bar)
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(TESTFILES_DIR, "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return jsonify({
            "message": "Sensitive value '{}' hashed and stored".format(encode_for_html(input_data.decode())),
        })

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new()")
        return jsonify({"error": str(e)}), 500

def do_something(param):
    thing = create_thing()
    return thing.do_something(param)

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    from html import escape
    return escape(data)

def create_thing():
    # Simulate the creation of a ThingInterface
    class ThingInterface:
        def do_something(self, param):
            return param  # Simulate processing

    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

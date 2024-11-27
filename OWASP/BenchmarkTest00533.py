
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00533", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    
    param = ""
    flag = True
    names = request.args.to_dict()
    for name, values in names.items():
        if flag:
            for value in values:
                if value == "BenchmarkTest00533":
                    param = name
                    flag = False

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    try:
        md = hashlib.sha1()
        input_param = bar.encode()
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('path/to/directory', 'passwordFile.txt')
        with open(file_target, 'ab') as fw:  # 'ab' will append the new data
            fw.write(b"hash_value=" + result + b"\n")

        response = (f"Sensitive value '{input_param.decode()}' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash")
        response = str(e)

    return response + "Hash Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

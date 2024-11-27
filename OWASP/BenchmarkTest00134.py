
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00134", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.headers.get("BenchmarkTest00134", "")

        param = os.path.basename(param)

        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        file_name = os.path.join('path/to/testfiles/dir', bar)

        try:
            # Create the file first (You might want to actually create a file if needed)
            with open(file_name, 'a'):
                pass
            
            return f"Now ready to write to file: {file_name}"
        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
            return "An error occurred", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00222", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = request
    param = ""
    for name in request.headers:
        if name in ["Content-Type", "User-Agent", "Accept"]:  # Simplified standard headers
            continue

        param = name
        break

    bar = None
    guess = "ABC"
    switchTarget = guess[2]

    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bobs_your_uncle"
    elif switchTarget in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    fileName = None
    fos = None

    try:
        fileName = os.path.join('path/to/testfiles', bar)
        fos = open(fileName, 'w')
        return f"Now ready to write to file: {fileName}"
    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{fileName}'")
    finally:
        if fos is not None:
            try:
                fos.close()
                fos = None
            except Exception as e:
                pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'

@app.route("/pathtraver-00/BenchmarkTest00362", methods=['GET', 'POST'])
def benchmark_test_00362():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00362', '')

        bar = param

        file_name = None
        fos = None

        try:
            file_name = os.path.join(TESTFILES_DIR, bar)

            with open(file_name, 'wb') as fos:
                return "Now ready to write to file: " + file_name

        except Exception as e:
            print("Couldn't open file: '" + str(file_name) + "'")
        finally:
            if fos is not None:
                try:
                    fos.close()
                except Exception:
                    pass
                
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

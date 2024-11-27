
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'  # Adjust the path as needed

@app.route("/pathtraver-01/BenchmarkTest01330", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01330', '')
        bar = Test().do_something(request, param)

        file_name = None
        fos = None

        try:
            file_name = os.path.join(TESTFILES_DIR, bar)
            fos = open(file_name, 'w')
            return f"Now ready to write to file: {html_escape(file_name)}"
        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        finally:
            if fos is not None:
                try:
                    fos.close()
                except Exception:
                    pass

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

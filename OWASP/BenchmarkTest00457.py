
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'  # Define your test files directory

@app.route("/pathtraver-00/BenchmarkTest00457", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ''
    param = request.args.get('BenchmarkTest00457', '')

    bar = ''
    if param:
        values_list = ['safe', param, 'moresafe']
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)
        fos = open(file_name, 'w')
        response += "Now ready to write to file: " + file_name
        
    except Exception as e:
        response += "Couldn't open FileOutputStream on file: '" + str(file_name) + "'"
        
    finally:
        if fos:
            try:
                fos.close()
            except Exception as e:
                pass

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

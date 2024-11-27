
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01908", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()  # Redirect GET to POST

    response = app.response_class()
    param = request.headers.get('BenchmarkTest01908', '')

    param = param.encode('utf-8').decode('utf-8')  # URL Decode the header value

    bar = do_something(param)

    file_name = os.path.join('testfiles', bar)
    is_stream = None

    try:
        with open(file_name, 'rb') as f:
            is_stream = f.read(1000)
            response.set_data(f"The beginning of file: '{escape_html(file_name)}' is:\n\n" +
                              escape_html(is_stream.decode('utf-8')))
    except Exception as e:
        response.set_data(f"Couldn't open InputStream on file: '{file_name}'\n" +
                          f"Problem getting InputStream: {escape_html(str(e))}")

    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ['safe', param, 'moresafe']
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

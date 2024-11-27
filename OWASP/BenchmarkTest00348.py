
from flask import Flask, request, make_response
import io

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00348", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response()
    
    if request.method == 'GET':
        return benchmark_test()

    input_data = request.get_data()
    str_value = input_data.decode('utf-8') if input_data else "No cookie value supplied"
    
    response.set_cookie('SomeCookie', str_value, secure=False, httponly=True, path=request.path)

    response_body = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"
    response.data = response_body.encode('utf-8')
    response.content_type = 'text/html;charset=UTF-8'
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

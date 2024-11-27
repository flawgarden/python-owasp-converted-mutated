
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

# Database setup
engine = create_engine('sqlite:///your_database.db')  # Update with your database

@app.route("/sqli-03/BenchmarkTest01813", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    param = request.args.get("BenchmarkTest01813")
    bar = Test().do_something(request, param)
    sql = "SELECT USERNAME FROM USERS WHERE USERNAME='foo' AND PASSWORD='{}'".format(bar)

    try:
        with engine.connect() as connection:
            result = connection.execute(sql).fetchone()
            response = "Your results are: " + encode_for_html(result[0])
    except NoResultFound:
        response = "No results returned for query: " + encode_for_html(sql)
    except Exception as e:
        response = "Error processing request."

    return response

class Test:
    def do_something(self, request, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        return "This should never happen"

def encode_for_html(value):
    # Function to encode value for HTML
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")  # Simplified encoding

if __name__ == '__main__':
    app.run(host='0.0.0.0')

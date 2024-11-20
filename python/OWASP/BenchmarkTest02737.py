
from flask import Flask, request, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.exc import NoResultFound

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    engine = create_engine('your_database_uri')
    connection = engine.connect()
    return connection

@app.route("/sqli-06/BenchmarkTest02737", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02737', '')

    bar = do_something(param)

    sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='{}'".format(bar)
    
    try:
        connection = get_db_connection()
        result = connection.execute(text(sql)).fetchall()
        connection.close()

        output = "Your results are: "
        for row in result:
            output += escape_html(row['USERNAME']) + " "
        return output

    except NoResultFound:
        return "No results returned for query: {}".format(escape_html(sql))
    except Exception as e:
        return "Error processing request."

def do_something(param):
    num = 86
    if (7 * 42) - num > 200:
        return "This_should_always_happen"
    else:
        return param

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

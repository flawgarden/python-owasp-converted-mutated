
from flask import Flask, request, render_template, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
DATABASE_URL = "your_database_url"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

@app.route("/sqli-06/BenchmarkTest02735", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = request.form.get("BenchmarkTest02735", "")

    bar = do_something(param)

    sql = "SELECT userid FROM USERS WHERE USERNAME='foo' AND PASSWORD=:bar"
    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql), {'bar': bar}).fetchone()
            if result:
                return jsonify(results=str(result[0]))
            else:
                return jsonify(message="No results returned for query: " + sql)
    except Exception as e:
        return jsonify(message="Error processing request.")

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

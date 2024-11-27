
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01313", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01313", "")
        
        bar = Test().do_something(request, param)

        sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

        try:
            statement = get_sql_statement()
            count = statement.execute_update(sql)
            output_update_complete(sql)
        except Exception as e:
            if hide_sql_errors:
                return "Error processing request."
            else:
                raise

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            del values_list[0]  # remove the 1st safe value

            bar = values_list[0]  # get the param value

        return bar

def get_sql_statement():
    # Implementation of database connection and statement retrieval
    pass

def output_update_complete(sql):
    # Implementation of outputting the completion of an update
    pass

hide_sql_errors = True

if __name__ == "__main__":
    app.run(host='0.0.0.0')

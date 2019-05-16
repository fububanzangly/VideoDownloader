from flask import Flask, render_template, request
import database
app = Flask(__name__)


@app.route('/')


def index():
    # arguments
    name = request.args.get('name')
    zimuzu = request.args.get('zimuzu')
    day = request.args.get('day')
    database.dump(name,zimuzu,day)
    print(database.load(day))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

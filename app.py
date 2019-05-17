from flask import Flask, render_template, request
import database
app = Flask(__name__)



@app.route('/')
def index():
    name = request.args.get('name')
    zimuzu = request.args.get('zimuzu')
    day = request.args.get('day')
    if name !="" and zimuzu !="" and name !=None and zimuzu !=None:
        database.dump(name,zimuzu,day)
        print(database.load(day))

    else:
        day=None
    result = database.load(day)
    print(result)
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run()

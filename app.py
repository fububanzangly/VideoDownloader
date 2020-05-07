from flask import Flask, render_template, request
import database
app = Flask(__name__)



@app.route('/')
def index():
    chinese = {'1': '一','2': '二','3': '三','4': '四','5': '五','6': '六','0': '日'}
    name = request.args.get('name')
    zimuzu = request.args.get('zimuzu')
    day = request.args.get('day')
    if name !="" and zimuzu !="" and name !=None and zimuzu !=None:
        database.dump(name,zimuzu,day)
        result = database.load(day)
        return render_template('index.html', result=result)
    else:
        result=[]
        for days in range(7):
            result.append("周"+chinese[str(days)])
            result.append(database.load(days))
        return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run()

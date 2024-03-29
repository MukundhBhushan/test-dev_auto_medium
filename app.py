from flask import render_template,request,Flask,redirect

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/posted',methods=['GET','POST'])
def posted():
    # name=request.form['name']
    # username=request.form['username']
    data={
        'name':request.form['name'],
        'username':request.form['username']
    }
    
    return render_template('posted.html',data=data)
if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0')
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'GreatGame'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    x= int(request.form['guess'])
    session['alert']=''
    if 'num' in session:
        r= session["num"]
    else:
        r=random.randint(1,101)
        session['num'] = r
    if 'attempts' in session:
        attempts= session["attempts"]
        session['attempts']+=1
    else:
        attempts=0
        session['attempts'] = attempts
    print(r)
    
    
    if r > x:
        session['alert']= 'too low!'
        print('too low!')
    elif r < x:
        session['alert']= 'too high!'
        print('too high!')
    elif r == x:
        session['alert']='That was the right number!!!'
        print('That was the right number!!!')
    over=''
    print('attempts', attempts)
    if attempts >= 6:
        over = 'Game Over'
        session['attempts'] = 0
        print('Game Over','number was', r)
        r=random.randint(1,101)
        session['num'] = r    
    return render_template('index.html', alert=session['alert'], over=over)



if __name__=="__main__":
    app.run(debug=True)
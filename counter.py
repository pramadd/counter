from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def count_visits(): # session[key] = value
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
       
    return render_template('index.html')

@app.route('/reload')
def count_reloads():
    if 'count' in session:
        session['count'] += 2
    else:
        session['count'] = session['count']
    return render_template('reload.html')

@app.route('/reset')
def reset_counter():
    if 'count' in session:
        session['count'] = 0
    else:
        session['count'] = session['count']
    return render_template('reset.html')




app.run(debug=True) 
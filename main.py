#!/usr/bin/env python
from concurrent.futures import process
from flask import Flask, flash, redirect, render_template, \
     request, url_for
from flask import Flask, session
from flask import Flask, session


app = Flask(__name__)
sess = session
app.secret_key = "super secret key"

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'Piyasiri'}, {'name':'Buddhika'}, {'name':'Vinuka'}])

@app.route("/input" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    session['key'] = select
    print(str(select))
    fileds = open(f"database/{session.get('username', 'not set')}.txt")
    filed = fileds.read()
    fileds.close()
    
    return(f"""Username: {str(select)}
<p><strong>Logged in as []</strong></p>
<p><strong>Click the button below to continue</strong></p>
<p><strong>පහත බොත්තම ක්ලික් කරන්න</strong></p>
<p><strong><a href="/formdat">Click here</a></strong></p>
Latest amounts:
{filed}""") # just to see what select is

@app.route('/formdat')
def my_form():
    return render_template('form.html')

@app.route('/formdat', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text =  (text)
    select = request.form.get('comp_select')
    username = session.get('key',None)
    with open(f"database/{username}.txt", 'r') as f:
        for line in f:
            pass
            last_line = line
            last_line = ((last_line))

    files = open(f"database/{username}.txt", 'w+')
    processed_text = (processed_text)
    current = int(processed_text)
    previous = int(last_line)
    files.write(f"{processed_text}")
    return(str(previous-current))
            

    
if __name__ == "__main__":


    app.debug = True
    app.run()
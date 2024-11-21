
import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.
                                     



@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('render_main')) # url_for('renderMain') could be replaced with '/'
    
    
@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/page1", methods=['GET', 'POST'])
def render_page1():
    return render_template('page1.html')
    
    
    
@app.route("/page2", methods=['GET', 'POST'])
def render_page2():
    session["1"]=request.form['question1']
    if "1"not in session:
        
        session["1"]=request.form['question1']
    
    return render_template('page2.html')
    
@app.route("/page3", methods=['GET', 'POST'])
def render_page3():
    if "2"not in session:
        
        session["2"]=request.form['question2']

    return render_template('page3.html')
    
@app.route("/page4", methods=['GET', 'POST'])
def render_page4():
    session["3"]=request.form['question3']
    if "3"not in session:
        
        session["3"]=request.form['question3']
    
    return render_template('page4.html')
    
@app.route("/answers", methods=['GET', 'POST'])
def render_page5():
    print (request.form)
    if "4"not in session:
        print ("hi")
        session["4"]=request.form['question4']
    print (session)
    session['score'] = 0
    if session["1"]== "The Legend of Zelda":
        first="Correct"  
        session['score'] +=1
    else:
        first="Wrong"
        
    
    
    if session["2"]== "Identify the impostor":
        second="Correct"
        session['score'] +=1
    else:     
        second="Wrong"
    
    
    if session["3"]== "Halo":
        third="Correct"
        session['score'] +=1
    else:
        third="Wrong"
    
   
    if session["4"]== "Pickaxe":
        fourth="Correct"
        session['score'] +=1
    else:
        fourth="Wrong"
    return render_template('answers.html',first=first, second=second, third=third, fourth=fourth, score=session['score'])
@app.route("/")
def render_main1():
    session['score'] = 0
    return render_template('home.html')
    
    
    


    
    
if __name__=="__main__":
    app.run(debug=True)
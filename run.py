from flask import Flask, url_for, redirect, render_template, request
from models import create_post, get_posts
from admin import create_post, get_posts

import sqlite3



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"



@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']

        ans = username + password
        print(ans)


        query = "SELECT username,password FROM post  WHERE username ='"+username+"' and password = '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            print("you have entered the wrong credentials please try again!!")

        else:
            return render_template("public/employee.html")    
 
    

    if request.method == 'POST':

        connection = sqlite3.connect("m_data.db")
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']

        ans = username + password
        print(ans)


        query = "SELECT username,password FROM user  WHERE username ='"+username+"' and password = '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            print("you have entered the wrong credentials please try again!!")

        else:
            return render_template("public/admin.html")    
 


       
    return render_template("public/index.html")

@app.route("/settings")
def settings():
    return render_template("/public/settings.html")    


@app.route("/admin")
def admin():
    return render_template("/public/admin.html")

@app.route("/sales")
def sales():
    return render_template("public/sales.html")

@app.route("/sales2")
def sales2():
    return render_template("public/sales2.html")    

@app.route("/trial")
def trial():
    return render_template("public/trial.html")


@app.route("/salesrecord")
def salesrecord():
    return render_template("public/salesrecord.html")


@app.route("/salesrecord2")
def salesrecord2():
    return render_template("public/salesrecord2.html")

@app.route("/inventory")
def inventory():
    return render_template("public/inventory.html")

@app.route("/employee")
def employee():
    return render_template("/public/employee.html")


@app.route("/eme")
def  eme():
    return render_template("public/eme.html") 




@app.route("/signup", methods= ["POST", "GET"])
def signup():

    if request.method == "GET":
        pass

    if request.method == "POST":

        Firstname = request.form.get('Firstname')
        Lastname = request.form.get('Lastname') 
        username = request.form.get('username') 
        password = request.form.get('password') 
        confirm_password = request.form.get('confirm_password') 
        create_post(Firstname, Lastname, username, password, confirm_password)
        
        if create_post == 0:
            print("fill in to signup")

        else:
            return redirect(url_for('index'))

    posts = get_posts()    
   


    return render_template("public/signup.html")


@app.route("/signup2")
def signup2():
    return render_template("public/signup2.html")

@app.route("/slogan")
def slogan():
    return render_template("public/slogan.html")



@app.route("/LoginForm", methods=["GET", "POST"])
def LoginForm():


    submissionform = signup()
    if request.method == 'POST':
        userName = ['name']
        password = ['password']

        ans = userName + password
        print(ans)
        connection = sqlite3.connect("us_database.db")
        cursor = connection.cursor()
        statement = f"SELECT * FROM users where Username ='{name}' AND password = '{password}'"
        cursor.execute(statement)
        
        result = cursor.fetchall()

        if len(result):
            print("you have not entered the right credentials")
        else:
            return render_template("public/LoginForm.html")    

    return render_template("public/LoginForm.html", loginform=loginform)




@app.route("/adminsign", methods= ["GET", "POST"])
def adminsign():

    if request.method == "GET":
       pass

    if request.method == "POST":

       Firstname = request.form.get('Firstname')
       Lastname = request.form.get('Lastname') 
       username = request.form.get('username') 
       password = request.form.get('password') 
       confirm_password = request.form.get('confirm_password') 
       create_post(Firstname, Lastname, username, password, confirm_password)
        
       if create_post == 0:
           print("fill in to signup")

       else:
           return redirect(url_for('index'))

    posts = get_posts()    
   

   


    return render_template("public/adminsign.html")





if __name__== "__main__":
   app.run(debug=True)

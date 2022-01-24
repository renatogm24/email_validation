from flask import render_template, request, redirect, flash

from flask_app.models import mail

from flask_app import app

@app.route('/')
def index():
    return render_template('/index.html') 

@app.route('/save', methods=["POST"])
def save():
    if not mail.Mail.validate_mail(request.form):
      return redirect('/')
    data = {
        "mail":request.form['mail'],
      }
    mail.Mail.save(data)
    flash("Mail added!")
    return redirect('/result') 

@app.route('/result')
def result():
    return render_template('/result.html',mails = mail.Mail.get_all()) 
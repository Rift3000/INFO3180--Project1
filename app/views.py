"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm
from app.models import UserProfile, Use
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from .models import MyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    myform = MyForm()

    if request.method == 'POST' and myform.validate_on_submit():
        firstname = myform.firstname.data
        lastname = myform.lastname.data
        gender = myform.gender.data
        email = myform.email.data
        location = myform.location.data
        bio = myform.bio.data
        photo = myform.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        d = datetime.datetime.today()
        dates = d.strftime("%d-%B-%Y")

        user = Use(first_name=firstname, last_name=lastname, gender=gender, email=email, location=location, bio=bio,
                   photo=filename, dates=dates)

        db.session.add(user)
        db.session.commit()

        users = Use.query.all()

        flash('You have successfully filled out the form', 'success')
        return render_template('profiles.html', filename=filename, firstname=firstname, lastname=lastname,
                               gender=gender, location=location, users=users)

    return render_template('add_profile.html', form=myform)


@app.route("/profiles")
def profiles():
    users = Use.query.all()

    return render_template('profiles.html', users=users)


@app.route("/profiles/<userid>")
def userProfiles(userid):
    users = Use.query.filter_by(id=userid).first()

    return render_template('userprofile.html', users=users)


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

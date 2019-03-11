from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/about')
def about():
    return render_template('about.html')


@page.route('/terms')
def terms():
    return render_template('terms.html')


@page.route('/privacy')
def privacy():
    return render_template('privacy.html')

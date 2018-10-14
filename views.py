from flask import Blueprint, render_template
from db import businesses

root = Blueprint('root', __name__, template_folder='templates')
@root.route('/')
def main():
    return render_template('index.html', company_name='Your Business Name')

from flask import Blueprint, render_template
from db import businesses

root = Blueprint('root', __name__, template_folder='templates')
@root.route('/')
def main():
    return render_template('index.html', company_name='Your Business Name')

business_pages = Blueprint('business_pages', __name__, template_folder='templates')
@business_pages.route('/<page>', strict_slashes=False)
def show(page):
    if page in business:
        company_name = businesses[page]['business_name']
        services = businesses[page]['services']
        img_src = businesses[page]['img_location']
    return render_template('listings.html', company_name=company_name, services=services, img_src=img_src)

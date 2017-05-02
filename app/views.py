from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	posts = [
		{
			'title' : '2 BHK flat for Rent in Alpine',
			'age' : '2',
			'flat_img' : 'flat',
			'rent' : '10000',
			'deposit' : '100000'
		},
		{
			'title' : '2 BHK flat for Rent in Alpine',
			'age' : '2',
			'flat_img' : 'flat',
			'rent' : '10000',
			'deposit' : '100000'
		},
		{
			'title' : '2 BHK flat for Rent in Alpine',
			'age' : '2',
			'flat_img' : 'flat',
			'rent' : '10000',
			'deposit' : '100000'
		}
	]
	return render_template('search-page.html', posts=posts)
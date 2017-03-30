from flask import render_template
from . import mod1

@mod1.route('/', defaults={'page':'index'})
@mod1.route('/<page>')
def show(page):
	return render_template('admin/index.html', page=page)
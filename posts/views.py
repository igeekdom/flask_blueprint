from flask import render_template
from . import mod2

@mod2.route('/', defaults={'page':'index'})
@mod2.route('/<page>')
def show(page):
	return render_template('/posts/index.html', page=page)
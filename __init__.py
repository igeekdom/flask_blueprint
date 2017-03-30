from flask import Flask, url_for

app = Flask(__name__)

from testapp.admin.views import mod1 as adminModule
from testapp.posts.views import mod2 as postsModule

app.register_blueprint(adminModule)
app.register_blueprint(postsModule)

@app.route('/')
def index():
	return "<a href='%s'>Admin Section</a> | \
			<a href='%s'>Posts Section</a>" % (url_for('admin.show'),
											  url_for('posts.show'))
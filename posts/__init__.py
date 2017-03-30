from flask import Blueprint

mod2 = Blueprint('posts', __name__, url_prefix='/posts', template_folder='templates')
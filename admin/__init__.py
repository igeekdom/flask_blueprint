from flask import Blueprint

mod1 = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates',)
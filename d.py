from flask import Blueprint

d = Blueprint('d', __name__)

@d.route('/')
def download():
	return 'qwer'
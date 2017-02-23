from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.sql import text

d = Blueprint('d', __name__)

eng = create_engine('mysql://root:rootpassword@localhost/maindb')

@d.route('/', methods=['GET'])
def download():
	last_id = request.args.get('last', 0, int)
	with eng.connect() as con:
		rs = con.execute("SELECT * FROM Downloads WHERE Id > " + last_id)
		line = rs.fetchall()
		return jsonify(line)


@d.route('/a', methods=['GET'])
def upload():
	with eng.connect() as con:

	    con.execute(text('DROP TABLE IF EXISTS Downloads'))
	    con.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY, 
	                 Link TEXT)'''))

	    data = (
	             { "Id": 1, "Link": "google" },
	             { "Id": 2, "Link": "google" },
	             { "Id": 3, "Link": "google" },
	             { "Id": 4, "Link": "google" }
	    )
	    for line in data:
	        con.execute(text("""INSERT INTO Downloads(Id, Link) 
	            VALUES(:Id, :Link)"""), **line)

	return 'SUCCESS'


from flask import Blueprint, request, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

d = Blueprint('d', __name__)

engine = create_engine('mysql://root:rootpassword@localhost/maindb')

Base = declarative_base
session = sessionmaker(bind=engine)()
 
class Links(Base):
    __tablename__ = 'downloads'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    link = Column(String(250), nullable=False)

def addlink(link):
	session.add(Links(link=link))
	session.commit()
def getlinks(id):
	return session.query(Links).filter(Links.id >= id).all()



@d.route('/', methods=['GET'])
def download():
	last_id = request.args.get('last', 0, int)
	return jsonify(getlinks(last_id))


@d.route('/a', methods=['GET'])
def upload():
	addLink('google')
	addLink('facebook')
	return 'Success'


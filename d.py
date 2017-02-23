from flask import Blueprint, request, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

d = Blueprint('d', __name__)

engine = create_engine('mysql://root:rootpassword@localhost/maindb')

Base = declarative_base()
session = sessionmaker(bind=engine)()
 
class Links(Base):
	__tablename__ = 'downloadtable'
	id = Column(Integer, primary_key=True)
	link = Column(String(250), nullable=False)
	def addlink(self):
		session.add(self)
		session.commit()
	@staticmethod
	def getlinks(id):
		return session.query(Links).filter(Links.id >= id).all()

#Base.metadata.create_all(engine)


@d.route('/', methods=['GET'])
def download():
	last_id = request.args.get('last', 0, int)
	objs = Links.getlinks(last_id)
	toReturn = ""
	for obj in objs:
		toReturn += ('\n' + str(obj.link))
	return toReturn


@d.route('/', methods=['POST'])
def upload():
	toAdd = request.form['link']
	Links(link=toAdd).addlink()
	return 'Success'


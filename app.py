
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask import request
from flask import jsonify

from db_init import Base, Client, Dataset

app = Flask(__name__)

@app.route("/client/", methods=['GET', 'POST', 'PUT'])
def client():
	# TODO move it to decorator
	engine = create_engine('sqlite:///data.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	
	if request.method == 'GET':
		clients = session.query(Client).all()
		return jsonify([])
	
	elif request.method == 'POST':
		name = request.args['name']
		ip_address = request.args['ip-address']
		client = Client(name=name, ip_address=ip_address)
		session.add(client)
		try:
			session.commit()
			return jsonify({'result':'success'})
		except:
			session.rollback()
			session.flush()
			return jsonify({'result':' failure'})
		
	elif request.method == 'PUT':
		return 'PUT'
    
	
@app.route("/client/<int:client_id>", methods=['GET', 'DELETE'])
def client_by_id(client_id):
	engine = create_engine('sqlite:///data.db')
	if request.method == 'GET':
		return 'GET'
	elif request.method == 'DELETE':
		return 'DELETE'

@app.route("/dataset/", methods=['GET', 'POST', 'PUT'])
def dataset():
	engine = create_engine('sqlite:///data.db')
	if request.method == 'GET':
		return 'GET'
	elif request.method == 'POST':
		return 'POST'
	elif request.method == 'PUT':
		return 'PUT'
    
	
@app.route("/dataset/<int:dataset_id>", methods=['GET', 'DELETE'])
def dataset_by_id(dataset_id):
	engine = create_engine('sqlite:///data.db')
	if request.method == 'GET':
		return 'GET'
	elif request.method == 'DELETE':
		return 'DELETE'

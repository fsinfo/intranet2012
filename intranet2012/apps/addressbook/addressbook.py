from flask import Blueprint, jsonify
from flaskext.login import login_required
import json

addressbook = Blueprint('addressbook', __name__, template_folder='templates/addressbook')

@addressbook.route('/index.json', methods=['GET', 'POST'])
@login_required
def addr_index():
	'''Returns a list of all entries'''
	return jsonify()

@addressbook.route('/tag/index.json', methods=['POST'])
def addr_new_tag():
	'''Create a new tag'''
	return jsonify()

@addressbook.route('/tag/<string:tag>.json', methods=['GET', 'PUT'])
def addr_tag(tag):
	'''Returns ??? of the given tag'''
	return jsonify()

@addressbook.route('/id/<int:aid>.json', methods=['GET', 'PUT', 'DELETE'])
def addr_id(aid):
	'''Returns the address with the given id'''
	return jsonify()

@addressbook.route('/id/<int:aid>.vcard', methods=['GET'])
@addressbook.route('/index.vcard', methods=['GET'])
def addr_vcard(aid=0):
	'''Returns the address with the given id as vcard. Returns all addresses as vcard if aid is 0'''
	return

@addressbook.route('/index.csv', methods=['GET'])
def addr_csv():
	'''Returns all addresses as comma seperated values file'''
	return

@addressbook.route('/user/<int:uid>.json', methods=['GET'])
def addr_user_info():
	'''Returns the address corresponding to the given user id'''
	return jsonify()

@addressbook.route('/search.json', methods=['GET', 'POST'])
def addr_search():
	'''Returns a filtered list of addresses'''
	return jsonify()

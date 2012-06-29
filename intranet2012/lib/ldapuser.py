import ldap
from ldap.cidict import cidict

basedn = "ou=users,dc=fachschaft,dc=informatik,dc=uni-kl,dc=de"

class LDAPUser(object):
	"""Wraps User object for Flask-Login"""
	def __init__(self, connection, user):
		print "LDAPUser:" + user
		result = connection.search_s( basedn, ldap.SCOPE_SUBTREE, '(cn=' + user + ')', ['uid' ] )
		print "LDAPResult:"
		print result
		if len(result) == 1:
			self._attrs = cidict(result[0][1])

	def get_id(self):
		return unicode(self._attrs['uid'][0])

	def is_active(self):
		res = True
		try:
			self._attrs
		except AttributeError:
			res = False
		return res #TODO

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	def authenticate(self, connection, password):
		try:
			result = connection.simple_bind_s( 'cn=' + self._attrs['uid'][0] + ',ou=users,dc=fachschaft,dc=informatik,dc=uni-kl,dc=de', password)
			print result
		except ldap.INVALID_CREDENTIALS:
			print "Invalid credentials"
			return False
		return True

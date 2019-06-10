from graphene import ObjectType, String, Schema
import json
from datetime import datetime

class User(ObjectType):
	id = graphene.ID()
	username = graphene.String()
	last_login = graphene.DateTime()


class Query(ObjectType):
	# this defines a Field `hello` in our Schema with a single argument `name
	hello = String(name=String(default_value="stranger"))
	goodbye = String()

	# our resolver method takes the GraphQL context (root, info) as well as
	# Argument (name) for the Field and returns the data for the query Response
	def resolve_hello(root, info, name):
		return f'Hello {name}!'

	def resolve_goodbye(root, info):
		return 'See ya!'

	def resolve_users(root, info):
		return [
			User(username='Alice', last_login=datetime.now()),
			User(username='Bob', last_login=datetime.now())
		]

schema = Schema(query=Query)

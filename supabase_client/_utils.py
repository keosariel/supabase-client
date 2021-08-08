from .supebase_exceptions import InvalidRangeError, UnexpectedValueTypeError
import urllib.parse

class QueryBuilder:
	"""	
	Helps construct a valid url for making requests

	:param base_url: a valid url
	:type  base_url: String
	"""
	
	def __init__(self, base_url):
		self.url  = base_url
		self.vars = {}
		self.query_headers = {}

	@property
	def _as_url(self):
		return self.url +"?"+ urllib.parse.urlencode(self.vars)

	def __repr__(self):
		return self._as_url

class TableQueryBuilder(QueryBuilder):
	"""	
	Helps construct a valid url for making requests

	:param base_url: a valid url
	:type  base_url: String
	
	Example
	-------

	>>> querier = TableQueryBuilder("http://app-name.supabase.co")
	>>> querier.select("*").range(0,10)
	http://app-name.supabase.co?select=%2A
	>>>
	"""

	def __init__(self, base_url):
		super().__init__(base_url)
		self.vars.update({"select": "*"})

	def select(self, val):
		self.vars.update({"select": val})
		return self

	def range(self, start, end):
		if (type(start) is not int) or (type(end) is not int):
			raise UnexpectedValueTypeError("Expected type int for: `start` and `end`")

		if start > end:
			raise InvalidRangeError("`start` should be less than (<) than `end`")

		self.query_headers.update({"Range": f"{start}-{end}"})
		return self

	def eq(self, column, val):
		self.vars.update({column: f"eq.{val}"})
		return self

	def gt(self, column, val):
		if type(val) is not int:
			raise UnexpectedValueTypeError("Expected type int for: `val`")

		self.vars.update({column: f"gt.{val}"})
		return self

	def lt(self, column, val):
		if type(val) is not int:
			raise UnexpectedValueTypeError("Expected type int for: `val`")

		self.vars.update({column: f"lt.{val}"})
		return self

	def gte(self, column, val):
		if type(val) is not int:
			raise UnexpectedValueTypeError("Expected type int for: `val`")

		self.vars.update({column: f"gte.{val}"})
		return self

	def lte(self, column, val):
		if type(val) is not int:
			raise UnexpectedValueTypeError("Expected type int for: `val`")

		self.vars.update({column: f"lte.{val}"})
		return self

	def like(self, column, val):
		self.vars.update({column: f"like.{val}"})
		return self

	def ilike(self, column, val):
		self.vars.update({column: f"ilike.{val}"})
		return self

	def neq(self, column, val):
		self.vars.update({column: f"neq.{val}"})
		return self

	def _is(self, column, val):
		raise NotImplementedError

	def _in(self, column, val):
		raise NotImplementedError

	def cs(self, column, val):
		raise NotImplementedError

	def cd(self, column, val):
		raise NotImplementedError


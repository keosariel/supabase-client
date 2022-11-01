from .supebase_exceptions import (
	InvalidRangeError, UnexpectedValueTypeError, QueryError)
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
		"""
        Limits the result to rows within the specified range, inclusive.
   
        :param start:  The starting index from which to limit the result, inclusive.
        :param end:  The last index to which to limit the result, inclusive.
		"""
		if (type(start) is not int) or (type(end) is not int):
			raise UnexpectedValueTypeError("Expected type int for: `start` and `end`")

		if start > end:
			raise InvalidRangeError("`start` should be less than (<) than `end`")

		self.query_headers.update({"Range": f"{start}-{end}"})
		return self

	def eq(self, column, val):
		"""
		Finds all rows whose value on the stated `column` exactly matches the
		specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""
		self.vars.update({column: f"eq.{val}"})
		return self

	def neq(self, column, val):
		"""
		Finds all rows whose value on the stated `column` doesn't match the
        specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The pattern to filter with.
		"""
		self.vars.update({column: f"neq.{val}"})
		return self

	def gt(self, column, val):
		"""
		Finds all rows whose value on the stated `column` is greater than the
   		specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""

		self.vars.update({column: f"gt.{val}"})
		return self

	def lt(self, column, val):
		"""
		Finds all rows whose value on the stated `column` is less than the
		specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""

		self.vars.update({column: f"lt.{val}"})
		return self

	def gte(self, column, val):
		"""
		Finds all rows whose value on the stated `column` is greater than or
   		equal to the specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""

		self.vars.update({column: f"gte.{val}"})
		return self

	def lte(self, column, val):
		"""
		Finds all rows whose value on the stated `column` is less than or
   		equal to the specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""

		self.vars.update({column: f"lte.{val}"})
		return self

	def like(self, column, pattern):
		"""
		Finds all rows whose value in the stated `column` matches the supplied
   		`pattern` (case sensitive).
		
		:param column:  The column to filter on.
		:param pattern:  The pattern to filter with.
		"""
		self.vars.update({column: f"like.{pattern}"})
		return self

	def ilike(self, column, pattern):
		"""
		Finds all rows whose value in the stated `column` matches the supplied
        `pattern` (case insensitive).
		
		:param column:  The column to filter on.
		:param pattern:  The pattern to filter with.
		"""
		self.vars.update({column: f"ilike.{val}"})
		return self

	def _is(self, column, val):
		"""
		A check for exact equality (null, true, false), finds all rows whose
        value on the stated `column` exactly match the specified `val`.
		
		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""
		self.vars.update({column: f"is.{val}"})
		return self

	def _in(self, column, vals):
		"""
		Finds all rows whose value on the stated `column` is found on the
        specified `vals`.

		:param column:  The column to filter on.
		:param vals:  The pattern to filter with.
		"""
		self.vars.update({column: f"in.({val})"})
		return self

	def cs(self, column, val):
		"""
		# contains
		Finds all rows whose json, array, or range value on the stated `column`
        contains the values specified in `val`.

		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""
		if type(val) == str:
			self.vars.update({column: f"cs.{{{val}}}"})
		elif type(val) == list:
			self.vars.update({column: f"cs.{{{','.join(val)}}}"})
		else:
			if type(val) is not int:
				raise UnexpectedValueTypeError("Expected type list or str for: `val`")

		return self

	def cd(self, column, val):
		"""
		# containedBy
		Finds all rows whose json, array, or range value on the stated `column` is
        contained by the specified `val`.

		:param column:  The column to filter on.
		:param val:  The value to filter with.
		"""
		if type(val) == str:
			self.vars.update({column: f"cd.{{{val}}}"})
		elif type(val) == list:
			self.vars.update({column: f"cd.{{{','.join(val)}}}"})
		else:
			if type(val) is not int:
				raise UnexpectedValueTypeError("Expected type list or str for: `val`")

		return self

	def limit(self, count):
		"""
	    Limits the result with the specified `count`.
	 
	    :param count:  The maximum no. of rows to limit to.
		"""
		if type(count) is not int:
			raise UnexpectedValueTypeError("Expected type int for: `count`")

		self.vars.update({"limit": count})
		return self

	def order_by(self, column, ascending=True, nullsFirst=False):
		"""
        Orders the result with the specified `column`.
   
        :param column:  The column to order on.
        :param ascending:  If `True`, the result will be in ascending order.
        :param nullsFirst:  If `True`, `null`s appear first.
		"""

		order = "asc" if ascending else "desc"
		order_for_nulls = "nullsfirst" if nullsFirst else "nullslast"

		self.vars.update({"order": f"{column}.{order}.{order_for_nulls}"})
		return self

	def csv(self):
		self.query_headers.update({"Accept": "text/csv"})
		return self


"""Internal HTTP client module.

This module provides utilities for making HTTP calls using the aiohttp library.
"""

import aiohttp

DEFAULT_TIMEOUT_CONFIG = aiohttp.ClientTimeout(total=60, connect=None,
                      sock_connect=None, sock_read=None)

class HTTPClient:

	"""Base HTTP client used to make HTTP calls.

    HTTPClient maintains an HTTP session, and handles request authentication and retries if
    necessary.
    """

	def __init__(self, url='', headers={},
		timeout=DEFAULT_TIMEOUT_CONFIG, **kwargs):

		self.url = url
		self.headers = headers
		self.timeout = timeout
		self._session = None

	async def requests(self, method, url="", **kwargs):
		"""Makes an HTTP call using the Python aiohttp library.

        This is the sole entry point to the requests library. All other helper methods in this
        class call this method to send HTTP requests out. Refer to

        :param method: HTTP method name as a string (e.g. GET, POST).
        :param url: URL of the remote endpoint.
        :param kwargs: An additional set of keyword arguments to be passed into the requests API
              (e.g. json, data, headers).

        :return: An HTTP response object and possibly the response JSON.

        :raises: NotImplementedError
        """

		method = method.upper()
		if method not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
			raise NotImplementedError(f"Method '{method}' not recognised.")

		if method == "GET":
			request_func = self._session.get
		elif method == "POST":
			request_func = self._session.post
		elif method == "PUT":
			request_func = self._session.put
		elif method == "PATCH":
			request_func = self._session.patch
		elif method == "DELETE":
			request_func = self._session.delete

		async with request_func(self.url, headers=self.headers, **kwargs) as response:
			data = await response.json() if method != "DELETE" else None
			return response, data

		return None, None

	async def __aenter__(self):
		self._session = aiohttp.ClientSession(timeout=self.timeout)
		return self

	async def __aexit__(self, *args):
		await self._session.close()
		self._session = None
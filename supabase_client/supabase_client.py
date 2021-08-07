from ._http_client import HTTPClient
from ._supabase_clients import TableClient

class Client:

    def __init__(self, api_url, api_key, headers={}):
        """
        Instantiate the client.

        :param supabase_url: The URL to the Supabase instance that should be connected to.
        :type  supabase_url: String
        :param supabase_key: The API key to the Supabase instance that should be connected to.
        :type  supabase_key: String
        """

        if not api_url:
            raise Exception("Supabase API-URL  is required")
        
        if not api_key:
            raise Exception("Supabase API-KEY is required")

        self.api_url = api_url
        self.api_key = api_key
        self.rest_url: str = f"{api_url}/rest/v1"

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            **headers,
        }


    def table(self, name):
        """
        Create a Instance of a query-able table
        
        :param name: an existing table
        :type  name: String

        :return: class instance `_supabase_clients.TableClient`
        """

        # Adding Authentication Headers
        self.headers.update(self._get_auth_headers)

        table_client = TableClient(
            api_url    = self.rest_url,
            table_name = name,
            headers    = self.headers
        )

        return table_client

    @property
    def _get_auth_headers(self):
        """Helper method to get auth headers."""

        headers =  {
            "apiKey": self.api_key,
            "Authorization": f"Bearer {self.api_key}",
        }
        return headers



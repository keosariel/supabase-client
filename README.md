# supabase-client
A Supabase client for Python. This mirrors the design of [supabase-js](https://github.com/supabase/supabase-js/blob/master/README.md)

[Full documentation: https://keosariel.github.io/2021/08/08/supabase-client-python/](https://keosariel.github.io/2021/08/08/supabase-client-python/)

## Overview
[Supabase](https://supabase.io/) is an Open Source Firebase Alternative that provides the tools and infrastructure you need to develop apps. It lets you
create a backend in less than 2 minutes. The **Supabase-Client** abstracts access the endpoints to the READ, INSERT, UPDATE, and DELETE operations on an existing **table** in your supabase application.

However, this project is base on the [Supabase API](https://supabase.io/docs/guides/api)

## Installation
To install Supabase-Client, simply execute the following command in a terminal:
```
pip install supabase-client
```

## Initializing
You can initialize a new Supabase client using the Client() method.

The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with the Supabase ecosystem.

### Example
```python
# requirement: pip install python-dotevn
from supabase_client import Client
from dotenv import dotenv_values
config = dotenv_values(".env")

supabase = Client( 
	api_url=config.get("SUPABASE_URL"),
	api_key=config.get("SUPABASE_KEY")
)
```

## Reading Data
### Fetch data: `select()`
```python
# Note: inside an async function
error, results = await (
     supabase.table("cities")
     .select("*")
     .query()
)
```
### Adding limits: `limit()`
```python
# Note: inside an async function
error, results = await (
     supabase.table("cities")
     .select("*")
     .limit(5)
     .query()
)
```
## Filters
```python
# Note: inside an async function
error, results = await (
     supabase.table("cities")
     .select("*")
    # Filters
    # .eq('column', 'Equal to')
    # .gt('column', 'Greater than')
    # .lt('column', 'Less than')
    # .gte('column', 'Greater than or equal to')
    # .lte('column', 'Less than or equal to')
    # .like('column', '%CaseSensitive%')
    # .ilike('column', '%CaseInsensitive%')
    # .neq('column', 'Not equal to')
    .query()
)
```
## Inserting Data
### Create data: `insert()`
```python
error, result = await (
      supabase.table("cities")
      .insert([{"name": "The Shire", "country_id": 554}])
)
```

## Modify data: `update()`
### Performs an UPDATE operation on the table.
```python
error, result = await (
      supabase.table("cities")
      .update(
      	{ 'name': 'Auckland' }, # Selection/Target column
      	{ 'name': 'Middle Earth' } # Update
      )
)
```
## Delete data: `delete()`
### Performs a DELETE operation on the table.
```python
error, result = await (
      supabase.table("cities")
      .delete({ 'name': 'Middle Earth' })
)
```

## License
Supabase-Client is licensed under the [MIT License](https://mit-license.org/)

See [Supabase Docs](https://supabase.io/docs/guides/api)

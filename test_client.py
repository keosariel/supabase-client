import asyncio
import unittest

from supabase_client.supabase_client import Client

from dotenv import dotenv_values
config = dotenv_values(".env")

def async_test(async_func):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_func(*args, **kwargs))
    return wrapper

class TestSupabaseClient(unittest.TestCase):

	supabase = Client(
		api_url=config.get("SUPABASE_URL"),
		api_key=config.get("SUPABASE_KEY")
	)

	@async_test
	async def test_read(self):
		error, results = await (
			self.supabase.table("posts")
			.select("*")
			.query()
		)

		if not error:
			self.assertEqual(type(results), list)

	@async_test
	async def test_insert(self):
		error, results = await (
			self.supabase.table("posts")
			.select("*")
			.query()
		)

		if not error:
			self.assertEqual(type(results), list)
			previous_length = len(results)

			error, result = await (
				self.supabase.table("posts")
				.insert([{"title": "test new title"}])
			)

			if not error:
				error, new_results = await (
					self.supabase.table("posts")
					.select("*")
						.query()
				)

				if not error:
					self.assertNotEqual(previous_length,len(new_results))

	@async_test
	async def test_update(self):
		_id = 1
		error, results = await (
			self.supabase.table("posts")
			.select("*")
			.eq("id", _id)
			.query()
		)

		if not error:
			self.assertEqual(type(results), list)
			if results:
				new_title  =  "updated title"
				error, result =  await (
					self.supabase.table("posts")
					.update({"id": f"eq.{_id}"},
						{"title":new_title}
					)
				)

				if not error:
					error, results = await (
						self.supabase.table("posts")
						.select("*")
						.eq("id", _id)
						.query()
					)

					if not error:
						if results:
							data = results[0]
							self.assertNotEqual(data.get("title"), new_title)

	@async_test
	async def test_delete(self):
		error, results = await (
			self.supabase.table("posts")
			.select("*")
			.query()
		)

		if not error:
			self.assertEqual(type(results), list)
			previous_length = len(results)

			error, result = await (
				self.supabase.table("posts")
				.delete({"title": "test new title"})
			)

			if not error:
				error, new_results = await (
					self.supabase.table("posts")
					.select("*")
					.query()
				)

				if not error:
					self.assertNotEqual(previous_length,len(new_results))


if __name__ == "__main__":
	unittest.main()
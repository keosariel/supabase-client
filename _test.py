import asyncio
from supabase_client import Client


from dotenv import dotenv_values
config = dotenv_values(".env")

supabase = Client(
		api_url=config.get("SUPABASE_URL"),
		api_key=config.get("SUPABASE_KEY")
)

async def main():
	pass

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
# notion_updater.py

from notion_client import Client
from datetime import datetime, timezone
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)


utc_now = datetime.now(timezone.utc).isoformat()

print("📡 Using DATABASE_ID:", DATABASE_ID)
print("🕒 Current UTC Time:", utc_now)


response = notion.databases.query(database_id=DATABASE_ID)
pages = response["results"]


for page in pages:
    page_id = page["id"]
    print("🔄 Updating page:", page_id)

    notion.pages.update(
        page_id=page_id,
        properties={
            "Now_UTC": {
                "date": {
                    "start": utc_now
                }
            }
        }
    )

print("✅ All pages updated with UTC time:", utc_now)

from notion_client import Client
from datetime import datetime
import os

# 从 GitHub Secret 中读取
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)

utc_now = datetime.utcnow().isoformat()

pages = notion.databases.query(database_id=DATABASE_ID)["results"]

for page in pages:
    print("Updating page:", page["id"]) 
    notion.pages.update(
        page_id=page["id"],
        properties={
            "Now_UTC": {
                "date": {
                    "start": utc_now
                }
            }
        }
    )

print("✅ Updated Now_UTC to", utc_now)
print("Using DATABASE_ID:", DATABASE_ID)

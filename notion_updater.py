from datetime import datetime, timezone
from notion_client import Client

notion = Client(auth=NOTION_TOKEN)

utc_now = datetime.now(timezone.utc).isoformat()

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

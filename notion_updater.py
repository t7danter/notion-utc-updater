from notion_client import Client
import os

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)

# 获取页面列表
pages = notion.databases.query(database_id=DATABASE_ID)["results"]

print("Pages found:", len(pages))

# 尝试更新第一个页面的 Test_Number = 1
for page in pages:
    page_id = page["id"]
    print("📝 Updating page:", page_id)

    try:
        notion.pages.update(
            page_id=page_id,
            properties={
                "Test_Number": {
                    "number": 1
                }
            }
        )
        print(f"✅ Successfully updated page: {page_id}")
        break  # 只改一条测试
    except Exception as e:
        print(f"❌ Failed to update page {page_id}: {e}")
        continue

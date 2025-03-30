# notion_updater.py

from notion_client import Client
from datetime import datetime, timezone
import os

# ✅ 从 GitHub Secrets 中读取环境变量
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["DATABASE_ID"]

# ✅ 初始化 Notion 客户端
notion = Client(auth=NOTION_TOKEN)

# ✅ 获取当前 UTC 时间，包含时区信息（ISO8601 格式 + Z）
utc_now = datetime.now(timezone.utc).isoformat()

print("📡 Using DATABASE_ID:", DATABASE_ID)
print("🕒 Current UTC Time:", utc_now)

# ✅ 查询数据库内容
response = notion.databases.query(database_id=DATABASE_ID)
pages = response["results"]

# ✅ 遍历并更新每条记录的 Now_UTC 字段
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
